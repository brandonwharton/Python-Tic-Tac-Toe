# A tic-tac-toe game
gameboard = {
    'top_row': {'left': ' ', 'middle': ' ', 'right': ' '},
    'middle_row': {'left': ' ', 'middle': ' ', 'right': ' '},
    'bottom_row': {'left': ' ', 'middle': ' ', 'right': ' '}
}

def run_game():
    global gameboard
    player1 = input('Player 1, input your name', )
    player2 = input('Player 2, input your name', )
    print(f'Hello {player1} and {player2} and welcome to tic-tac-toe.')
    build_board()


def build_board():
    global gameboard
    top = gameboard['top_row']
    middle = gameboard['middle_row']
    bottom = gameboard['bottom_row']
    print(f"{top['left']} | {top['middle']} | {top['left']}")
    print("_________")
    print(f"{middle['left']} | {middle['middle']} | {middle['left']}")
    print("_________")
    print(f"{bottom['left']} | {bottom['middle']} | {bottom['left']}")


run_game()


