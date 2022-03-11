import time

from Rules import Player
from Rules import ComputerPlayer
import random

rows_number = 3
columns_number = 3
diagonals_number = 2
blank = "-"
row_1 = 1
row_2 = 4
row_3 = 7

reference_board = [
    [row_3 + i for i in range(rows_number)],
    [row_2 + i for i in range(rows_number)],
    [row_1 + i for i in range(rows_number)]
]

game_board = [
    [blank for i in range(rows_number)],
    [blank for i in range(rows_number)],
    [blank for i in range(rows_number)]
]

player1 = Player(game_board, input("Player 1 enter your username: ").upper())
ref_board = Player(reference_board, "0")

# Decides if player 2 will be an AI or a human player
player2_username = input("Player 2 enter your username: ").upper()

if player2_username == "AI":
    player2 = ComputerPlayer(game_board, player2_username)
    possible_moves = [i + 1 for i in range(9)]  # List of moves the AI will be able to do.
else:
    player2 = Player(game_board, player2_username)



def player_details():
    print("Reference board")
    ref_board.get_board()
    print("Tic Tac Toe")
    player1.get_board()


def check_rows(playerName, playerSymbol):

    win = f'{playerSymbol}{playerSymbol}{playerSymbol}'

    for i in range(rows_number):
        row = ''.join(player1.get_row(i))
        if row == win:
            print("Tic Tac Toe")
            player1.get_board()
            print(f"\n{playerName} wins")
            return True


def check_columns(playerName, playerSymbol):

    win = f'{playerSymbol}{playerSymbol}{playerSymbol}'

    for i in range(columns_number):
        column = ''.join(player1.get_column(i))
        if column == win:
            print("Tic Tac Toe")
            player1.get_board()
            print(f"\n{playerName} wins")
            return True


def check_diagonals(playerName, playerSymbol):

    win = f'{playerSymbol}{playerSymbol}{playerSymbol}'

    for i in range(diagonals_number):
        diagonal = ''.join(player1.get_diagonal(i))
        if diagonal == win:
            print("Tic Tac Toe")
            player1.get_board()
            print(f"\n{playerName} wins")
            return True


def play():

    # Players choose symbols (X or O)
    played_position = ["" for i in range(9)]
    counter = 0

    while True:
        player1_symbol = input(f"{player1.get_player_name()} choose your symbol (O or X): ")
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

    # Players choose their position of play
    while True:
        try:

            # Player 1 conditions to play
            flag1 = True
            while flag1:
                player_details()
                player1_input = int(input(f"{player1.get_player_name()} choose a position from 1 to 9: "))

                if player1_input in played_position:
                    print("This position has already been played\nRetry !")

                elif player1_input in range(1,10):
                    if player2_username == "AI":
                        player2.deleteMove(possible_moves, player1_input)
                    flag1 = False
                    player1.set_board(player1_input, player1_symbol.upper())
                    played_position[counter] = player1_input
                    counter += 1
                    print(f"played position {played_position}")

                    # Checks if the player wins the game or if tie
                    if check_rows(player1.get_player_name(), player1_symbol.upper()) \
                            or check_columns(player1.get_player_name(), player1_symbol.upper())\
                            or check_diagonals(player1.get_player_name(), player1_symbol.upper()):
                        return True
                    elif counter >= 9:
                        player_details()
                        print("\n Tie")
                        return True
                else:
                    print("Wrong input !")

            # Player 2 conditions to play
            flag2 = True
            while flag2:
                player_details()

                if player2_username == "AI":
                    player2_input = random.choice(possible_moves)
                else:
                    player2_input = int(input(f"{player2.get_player_name()} choose a position from 1 to 9: "))

                if player2_input in played_position:
                    print("This position has already been played\nRetry")

                elif player2_input in range(1,10):
                    if player2_username == "AI":
                        player2.deleteMove(possible_moves, player2_input)
                        time.sleep(0.5)
                    flag2 = False
                    player2.set_board(player2_input, player2_symbol.upper())
                    played_position[counter] = player2_input
                    counter += 1
                    print(f"played position {played_position}")

                    # Checks if the player wins the game or if tie
                    if check_rows(player2.get_player_name(), player2_symbol.upper())\
                            or check_columns(player2.get_player_name(), player2_symbol.upper())\
                            or check_diagonals(player2.get_player_name(), player2_symbol.upper()):
                        return True
                    elif counter >= 9:
                        player_details()
                        print("\n Tie")
                        return True
                else:
                    print("Wrong input !")

        except(ValueError):
            print("Wrong input")








play()