import connectfour
import connectfour_methods as methods

def game():
    '''Plays the console version of the connect four game.'''
    gamestate = connectfour.new_game()
    while connectfour.winner(gamestate) == connectfour.NONE:
        methods.getBoard(gamestate)
        while True:
            choice = methods.popOrDrop()
            col = methods.columnChoice()
            try:
                gamestate = methods.move(gamestate, col, choice)
                methods.getBoard(gamestate)
            except connectfour.InvalidMoveError:
                print('That is an invalid move.')
                break
            except connectfour.GameOverError:
                print('The game is already over.')
                break
    methods.printWinner(gamestate)


if __name__ == '__main__':
    game()
                
