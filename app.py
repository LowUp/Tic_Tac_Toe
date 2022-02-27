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
player2 = Rules(game_board)
ref_board = Rules(reference_board)

def player_details():
    print("Reference board")
    ref_board.get_board()
    print("Tic Tac Toe")
    player1.get_board()

def play():

    played_position = ["" for i in range(9)]
    counter = 0

    while True:
        player1_symbol = input("Player 1 choose your symbol (O or X): ")
        if (player1_symbol == "O" or player1_symbol == "o") or (player1_symbol == "X" or player1_symbol == "x"):
            print("Success")
            if player1_symbol == "O" or player1_symbol == "o":
                player2_symbol = "X"
                break
            else:
                player2_symbol = "O"
                break
        else:
            print("Wrong input! \nTry again !")
    while True:
        try:
            flag1 = True
            while flag1:
                player_details()
                player1_input = int(input(f"Player 1 choose a position from 1 to 9: "))

                if player1_input in played_position:
                    print("This position has already been played\nRetry !")

                else:
                    flag1 = False
                    player1.set_board(player1_input, player1_symbol.upper())
                    played_position[counter] = player1_input
                    counter += 1
                    print(f"played position {played_position}")

            flag2 = True
            while flag2:
                player_details()
                player2_input = int(input("Player 2 choose a position from 1 to 9: "))

                if player2_input in played_position:
                    print("This position has already been played\n Retry")
                else:
                    flag2 = False
                    player2.set_board(player2_input, player2_symbol.upper())
                    played_position[counter] = player2_input
                    counter += 1
                    print(f"played position {played_position}")

        except(ValueError):
            print("Wrong input")








play()