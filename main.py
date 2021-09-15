# A tic-tac-toe game

# Set up the gameboard data and current game status at the global scope
gameboard = {
    'top': {'left': ' ', 'middle': ' ', 'right': ' '},
    'middle': {'left': ' ', 'middle': ' ', 'right': ' '},
    'bottom': {'left': ' ', 'middle': ' ', 'right': ' '}
}

game_won = False


# Main function to start and run the game
def run_game():
    #### Setup ####
    global gameboard
    global game_won

    player1 = input('Player 1, input your name', )
    player2 = input('Player 2, input your name', )
    # Start player1 as the active player, active_player changes throughout the game as moves are made
    active_player = player1

    #### Begin Game Prompts ####
    print(f'Hello {player1} and {player2} and welcome to tic-tac-toe.')
    build_board()
    print(f'''Please make a move by entering where you would like to go. Format should be row-column for 
        rows named top, middle, and bottom with columns named left, middle, right''')

    # Game Logic
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


# Function that prints out the current gameboard in the console when called
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


# Function that handles the logic and validation for taking game actions
def make_move(name, symbol):
    global gameboard

    # Required formatting for moves matches the dictionary values: top, middle and bottom for rows, and left, middle
    # and right for columns. Moves must be entered as an input in row-column format matching those key names
    move = input(f"{name}, please make a move")

    # First validation - Make sure values are separated by a hyphen
    if '-' not in move:
        print('Please use a hyphen to separate your row and column selections: Example top-right or middle-middle')
        make_move(name, symbol)

    # Remove whitespace and save the move as a list in [row_name, column_name] format in lowercase
    split_move = move.lower().replace(' ', '').split('-')

    row = split_move[0]
    column = split_move[1]

    # Validate move selection to ensure proper formatting of move input from user
    if row not in ['top', 'middle', 'bottom'] or column not in ['left', 'middle', 'right'] or gameboard[row][column] != ' ':

        # Find list of available moves and save them
        move_list = []
        for key in gameboard.keys():
            for value in gameboard[key]:
                if gameboard[key][value] == ' ':
                    move_list.append(f'{key}-{value}')

        print('That move is unavailable')
        print('Available moves:', *move_list)

        # Print error message and recur the function
        # print('Invalid entry: Please try again')
        make_move(name, symbol)

    # Set the move chosen to the active player's symbol
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


