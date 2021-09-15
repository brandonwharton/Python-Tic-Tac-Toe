# A tic-tac-toe game
gameboard = {
    'top': {'left': ' ', 'middle': ' ', 'right': ' '},
    'middle': {'left': ' ', 'middle': ' ', 'right': ' '},
    'bottom': {'left': ' ', 'middle': ' ', 'right': ' '}
}

current_is_x = True

def run_game():
    global gameboard
    player1 = input('Player 1, input your name', )
    player2 = input('Player 2, input your name', )
    game_won = False
    active_player = player1


    print(f'Hello {player1} and {player2} and welcome to tic-tac-toe.')
    build_board()
    print(f'''Please make a move by entering where you would like to go. Format should be row-column for 
        rows named top, middle, and bottom with columns named left, middle, right''')

    while game_won == False:
        if current_is_x:
            make_move(player1)
        else:
            make_move(player2)

        build_board()


def build_board():
    global gameboard
    top = gameboard['top']
    middle = gameboard['middle']
    bottom = gameboard['bottom']
    print(f"{top['left']} | {top['middle']} | {top['right']}")
    print("_________")
    print(f"{middle['left']} | {middle['middle']} | {middle['right']}")
    print("_________")
    print(f"{bottom['left']} | {bottom['middle']} | {bottom['right']}")

def make_move(name):
    global gameboard
    global current_is_x

    move = input(f"{name}, please make a move")
    split_move = move.replace(' ', '').split('-')

    row = split_move[0]
    column = split_move[1]

    print('Row, column', row, column)

    if current_is_x:
        gameboard[row][column] = 'X'
    else:
        gameboard[row][column] = 'O'

    current_is_x = not current_is_x




run_game()


