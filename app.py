from Rules import Player

colomn_range = 3
rows_number = 3
columns_number = 3
diagonals_number = 2
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

player1 = Player(game_board, input("Player 1 enter your username: "))
player2 = Player(game_board, input("Player 2 enter your username: "))
ref_board = Player(reference_board, "0")


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
            print(f"\n{playerName} WINS")
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
            flag1 = True
            while flag1:
                player_details()
                player1_input = int(input(f"{player1.get_player_name()} choose a position from 1 to 9: "))

                if player1_input in played_position:
                    print("This position has already been played\nRetry !")

                elif player1_input in range(1,10):
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

            flag2 = True
            while flag2:
                player_details()
                player2_input = int(input(f"{player2.get_player_name()} choose a position from 1 to 9: "))

                if player2_input in played_position:
                    print("This position has already been played\nRetry")
                elif player2_input in range(1,10):
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