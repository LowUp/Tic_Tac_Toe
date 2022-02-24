import random
from Rules import Rules

colomn_range = 3
blank = "-"
row_1 = 1
row_2 = 4
row_3 = 7

reference_board = [
    [row_3 + i for i in range(colomn_range)],
    [row_2 + i for i in range(colomn_range)],
    [row_1 + i for i in range(colomn_range)]
]

game_board = [
    [blank for i in range(colomn_range)],
    [blank for i in range(colomn_range)],
    [blank for i in range(colomn_range)]
]

player1 = Rules(game_board)
ref_board = Rules(reference_board)

def play():

    symbol = ""

    while True:
        symbol = input("Choose your symbol (O or X): ")
        if (symbol == "O" or symbol == "o") or (symbol == "X" or symbol == "x"):
            print("Success")
            break
        else:
            print("Wrong input! \nTry again !")
    while True:
        try:
            print("Reference board")
            ref_board.get_board()
            print("Tic Tac Toe")
            player1.get_board()
            player_input = int(input("Choose a position from 1 to 9: "))
            player1.set_board(player_input, symbol.upper())
            if player_input == "y":
                break
        except(ValueError):
            print("Wrong input")








play()