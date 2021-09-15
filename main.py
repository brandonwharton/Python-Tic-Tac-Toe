# A tic-tac-toe game
gameboard = {
    'top': {'left': ' ', 'middle': ' ', 'right': ' '},
    'middle': {'left': ' ', 'middle': ' ', 'right': ' '},
    'bottom': {'left': ' ', 'middle': ' ', 'right': ' '}
}

game_won = False

def run_game():
    global gameboard
    global game_won

    player1 = input('Player 1, input your name', )
    player2 = input('Player 2, input your name', )
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
            game_over(active_player)
        elif middle['left'] == middle['middle'] == middle['right'] and middle['left'] != ' ':
            game_over(active_player)
        elif bottom['left'] == bottom['middle'] == bottom['right'] and bottom['left'] != ' ':
            game_over(active_player)
        elif top['left'] == middle['left'] == bottom['left'] and top['left'] != ' ':
            game_over(active_player)
        elif top['middle'] == middle['middle'] == bottom['middle'] and top['middle'] != ' ':
            game_over(active_player)
        elif top['right'] == middle['right'] == bottom['right'] and top['right'] != ' ':
            game_over(active_player)
        elif top['left'] == middle['middle'] == bottom['right'] and top['left'] != ' ':
            game_over(active_player)
        elif top['right'] == middle['middle'] == bottom['left'] and top['right'] != ' ':
            game_over(active_player)

        # If game hasn't been won, switch active player before loop ends
        if active_player == player1:
            active_player = player2
        else:
            active_player = player1

    # Loop is now finished, prompt another game or end program
    answer = input('Would you like to play again? Answer y for yes, anything else for no', )
    if (answer == 'y'):
        reset_game()
        run_game()


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

    move = input(f"{name}, please make a move")
    split_move = move.replace(' ', '').split('-')

    row = split_move[0]
    column = split_move[1]

    gameboard[row][column] = symbol


# Function to end game
def game_over(player):
    global game_won
    print(f"{player} Won!")
    game_won = True

def reset_game():
    global gameboard
    global game_won

    gameboard = {
        'top': {'left': ' ', 'middle': ' ', 'right': ' '},
        'middle': {'left': ' ', 'middle': ' ', 'right': ' '},
        'bottom': {'left': ' ', 'middle': ' ', 'right': ' '}
    }
    game_won = False

run_game()


