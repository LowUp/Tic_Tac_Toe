import random
from Rules import Rules

colomn_range = 3
blank = "-"

game_board = [
    [blank for i in range(colomn_range)],
    [blank for i in range(colomn_range)],
    [blank for i in range(colomn_range)]
]

player1 = Rules(game_board)

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
        player1.get_board()
        player_input = int(input("Choose a position from 1 to 9"))
        player1.set_board(player_input, symbol)
        







play()