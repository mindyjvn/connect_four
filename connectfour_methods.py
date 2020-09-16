import connectfour

def getBoard(gamestate):
    '''Display the board on the console.'''
    if gamestate.turn == connectfour.RED:
        print('It is Red\'s turn.')
    elif gamestate.turn == connectfour.YELLOW:
        print('It is Yellow\'s turn.')
        
    for column in range(connectfour.BOARD_COLUMNS):
        print(column + 1,end = '  ')
    print()

    for r in range(connectfour.BOARD_ROWS):
        for c in range(connectfour.BOARD_COLUMNS):
            if gamestate.board[c][r] == connectfour.NONE:
                print(".", end = '  ')
            elif gamestate.board[c][r] == connectfour.RED:
                print("R", end = '  ')
            elif gamestate.board[c][r] == connectfour.YELLOW:
                print("Y", end = '  ')
        print()
    print()


def popOrDrop():
    '''Prompt user to pop or drop. Return response.'''
    while True:
        userPD = input('Would you like to pop or drop?\n')
        if userPD.lower() == 'pop' or userPD.lower() == 'drop':
            return userPD.upper()
        else:
            print('Please select either pop or drop.')
        

def columnChoice():
    '''Prompt user to pick a valid column. Return response.'''
    while True:
        userColumn = input('Which column would you like to pop/drop?\n')
        if not str(userColumn).isdigit():
            print('Please enter a number.')
        elif connectfour._is_valid_column_number(int(userColumn)-1):
            return int(userColumn)
        else:
            print('Please select one of the columns displayed.')


def move(gamestate, col, choice):
    '''Executes the move.'''
    if choice.upper() == 'DROP':
        return connectfour.drop(gamestate, col - 1)
    elif choice.upper() == 'POP':
        return connectfour.pop(gamestate, col - 1)


def printWinner(gamestate):
    '''Prints the winner.'''
    if connectfour.winner(gamestate) == connectfour.RED:
        print('Red won!')
    elif connectfour.winner(gamestate) == connectfour.YELLOW:
        print('Yellow won!')

