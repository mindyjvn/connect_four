import connectfour
import connectfour_methods as methods
import connectfour_protocol as protocol

HOST = 'circinus-32.ics.uci.edu'
PORT = 4444

def getUsername():
    '''Asks user for a username. Built based off of method in protocol notes.'''
    while True:
        username = input('Username (without spaces): ').strip()

        if len(username) > 0 and ' ' not in username:
            return username
        else:
            print('Invalid username; please try again')

def playGame():
    '''Starts the connectfour game.'''
    username = getUsername()
    connection = protocol.connect(username, HOST, PORT)

    #start the game
    protocol.writeline(connection, 'I32CFSP_HELLO ' + username)
    protocol.readstream(connection)
    protocol.writeline(connection, 'AI_GAME')
    protocol.readstream(connection)
    
    gamestate = connectfour.new_game()

    while connectfour.winner(gamestate) == connectfour.NONE:
        #player's turn
        if gamestate.turn == connectfour.RED:
            methods.getBoard(gamestate)
            choice = methods.popOrDrop()
            col = methods.columnChoice()
            response = protocol.userMove(connection, choice, col)
            if response == 'closed':
                print('The connection to the server has been closed.')
                return
            elif response == 'invalid':
                print('That is an invalid move.')
            else:
                gamestate = methods.move(gamestate, col, choice)
        #server's turn
        else:
            methods.getBoard(gamestate)
            response = protocol.serverMove(connection)
            if response == 'closed':
                print('The connection to the server has been closed.')
                return
            else:
                choice = response[0]
                col = response[1]
                gamestate = methods.move(gamestate, col, choice)
        
    methods.printWinner(gamestate)
    protocol.close(connection)
    return
                

if __name__ == '__main__':
    playGame()
