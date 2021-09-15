# A tic-tac-toe game
gameboard = {
    'top_row': [' ', ' ', ' '],
    'middle_row': [' ', ' ', ' '],
    'bottom_row': [' ', ' ', ' ']
}

def run_game():
    global gameboard
    player1 = input('Player 1, input your name', )
    player2 = input('Player 2, input your name', )
    print(f'Hello {player1} and {player2} and welcome to tic-tac-toe.')

run_game()