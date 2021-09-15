# A tic-tac-toe game
gameboard = {
    'top': {'left': ' ', 'middle': ' ', 'right': ' '},
    'middle': {'left': ' ', 'middle': ' ', 'right': ' '},
    'bottom': {'left': ' ', 'middle': ' ', 'right': ' '}
}

current_is_x = True

def run_game():
    global gameboard
    global current_is_x
    player1 = input('Player 1, input your name', )
    player2 = input('Player 2, input your name', )
    game_won = False
    active_player = player1

    print(f'Hello {player1} and {player2} and welcome to tic-tac-toe.')
    build_board()
    print(f'''Please make a move by entering where you would like to go. Format should be row-column for 
        rows named top, middle, and bottom with columns named left, middle, right''')

    while game_won == False:
        if active_player == player1:
            make_move(player1, 'X')
        else:
            make_move(player2, 'O')

        build_board()

        top = gameboard['top']
        middle = gameboard['middle']
        bottom = gameboard['bottom']

        if top['left'] == top['middle'] == top['right'] and top['left'] != ' ':
            print(f"{player1} Won!")
            game_won = True

        if active_player == player1:
            active_player = player2
        else:
            active_player = player1


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

def make_move(name, symbol):
    global gameboard
    global current_is_x

    move = input(f"{name}, please make a move")
    split_move = move.replace(' ', '').split('-')

    row = split_move[0]
    column = split_move[1]

    gameboard[row][column] = symbol




run_game()


