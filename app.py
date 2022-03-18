import time

from Rules import Player
from Rules import ComputerPlayer
from Rules import UnbeatableAI
from Rules import Game

board1 = Game()

game_board = board1.game_board()

player1 = Player(game_board, input("Player 1 enter your username: ").upper())

# Decides if player 2 will be an AI or a human player
player2_username = input("Player 2 enter your username: ").upper()

if player2_username == "AI":
    choice = input("choose the difficulty level of the AI\n(e = easy) or (h = hard): ").upper()

    if choice == "H" or choice == "HARD":
        player2 = UnbeatableAI(game_board, player2_username)
    elif choice == "E" or choice == "EASY":
        player2 = ComputerPlayer(game_board, player2_username)
    else:
        print("Invalid input\nEasy will be selected by default")
        player2 = ComputerPlayer(game_board, player2_username)
else:
    player2 = Player(game_board, player2_username)


def player_details():
    board1.get_refBoard()
    board1.get_board()


def check_rows(player_name, player_symbol, display):
    rows_number = 3
    win = f'{player_symbol}{player_symbol}{player_symbol}'

    for i in range(rows_number):
        row = ''.join(board1.get_row(i))
        if row == win:
            if display:
                board1.get_board()
                print(f"\n{player_name} wins")
            return True


def check_columns(player_name, player_symbol, display):
    columns_number = 3
    win = f'{player_symbol}{player_symbol}{player_symbol}'

    for i in range(columns_number):
        column = ''.join(board1.get_column(i))
        if column == win:
            if display:
                board1.get_board()
                print(f"\n{player_name} wins")
            return True


def check_diagonals(player_name, player_symbol, display):

    diagonals_number = 2
    win = f'{player_symbol}{player_symbol}{player_symbol}'

    for i in range(diagonals_number):
        diagonal = ''.join(board1.get_diagonal(i))
        if diagonal == win:
            if display:
                board1.get_board()
                print(f"\n{player_name} wins")
            return True


def hard_mode_ai(board):
    best_score = -1000
    best_move = 0
    conteur = 0

    for key in range(1, 10):
        # print(board.board_keys(key))
        if board.board_keys(key).upper() == "-".upper():
            # print(board.board_keys(key))
            player2.set_board(key, player2.get_symbol(), False)
            score = minimax(board, 0, False, conteur)
            board.set_board(key, "-")
            if score > best_score:
                best_score = score
                best_move = key

    return best_move


def minimax(board, depth, is_maximizing, count):

    # checks if player 1 wins
    if check_rows(player1.get_player_name(), player1.get_symbol(), False) \
            or check_columns(player1.get_player_name(), player1.get_symbol(), False) \
            or check_diagonals(player1.get_player_name(), player1.get_symbol(), False):
        return -100

    # checks if player 2 wins
    elif check_rows(player2.get_player_name(), player2.get_symbol(), False) \
            or check_columns(player2.get_player_name(), player2.get_symbol(), False) \
            or check_diagonals(player2.get_player_name(), player2.get_symbol(), False):
        return 100

    # checks for draws
    elif board.draw():
        # I have to implement a function that make the computer understand when the game ties
        return 0

    # The computer plays against itself to check all the possibilities and choose the right one
    if is_maximizing:
        best_score = -1000

        for key in range(1, 10):
            if board.board_keys(key).upper() == "-".upper():
                player2.set_board(key, player2.get_symbol(), False)
                score = minimax(board, 0, False, count)
                board.set_board(key, "-")
                count += 1
                if score > best_score:
                    best_score = score

        return best_score

    else:
        best_score = 800

        for key in range(1, 10):
            if board.board_keys(key).upper() == "-".upper():
                player1.set_board(key, player1.get_symbol(), False)
                score = minimax(board, depth + 1, True, count)
                board.set_board(key, "-")
                count += 1
                if score < best_score:
                    best_score = score

        return best_score


def play():

    # Players choose symbols (X or O)
    played_position = ["" for i in range(9)]
    counter: int = 0

    while True:
        player1_symbol = input(f"{player1.get_player_name()} choose your symbol (O or X): ").upper()
        if player1_symbol == "O" or player1_symbol == "X":
            print("Success")
            if player1_symbol == "O":
                player1.set_symbol("O")
                player2.set_symbol("X")
                break
            else:
                player1.set_symbol("X")
                player2.set_symbol("O")
                break
        else:
            print("Wrong input! \nTry again !")

    # Players choose their position of play
    while True:

        # Player 1 conditions to play
        flag1 = True
        while flag1:
            player_details()
            try:
                player1_input = int(input(f"{player1.get_player_name()} choose a position from 1 to 9: "))
            except ValueError:
                print("Wrong input")

            if player1_input in played_position:
                print("This position has already been played\nRetry !")

            elif player1_input in range(1, 10):
                if player2_username == "AI":
                    player2.deleteMove(player1_input)
                flag1 = False
                player1.set_board(player1_input, player1.get_symbol(), True)
                played_position[counter] = player1_input
                counter += 1
                print(f"played position {played_position}")

                # Checks if the player wins the game or if tie
                if check_rows(player1.get_player_name(), player1.get_symbol(), True) \
                        or check_columns(player1.get_player_name(), player1.get_symbol(), True)\
                        or check_diagonals(player1.get_player_name(), player1.get_symbol(), True):
                    return player1.winner()
                elif board1.draw():
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
                if choice == "H" or choice == "HARD":
                    player2_input = player2.get_move(hard_mode_ai(board1))
                else:
                    player2_input = player2.get_move()
            else:
                try:
                    player2_input = int(input(f"{player2.get_player_name()} choose a position from 1 to 9: "))
                except ValueError:
                    print("Wrong input")

            if player2_input in played_position:
                print("This position has already been played\nRetry")

            elif player2_input in range(1, 10):
                if player2_username == "AI":
                    player2.deleteMove(player2_input)
                    time.sleep(0.5)
                if choice == "H" or choice == "HARD":
                    player2.deleteMove(player2_input)
                flag2 = False
                player2.set_board(player2_input, player2.get_symbol(), True)
                played_position[counter] = player2_input
                counter += 1
                print(f"played position {played_position}")

                # Checks if the player wins the game or if tie
                if check_rows(player2.get_player_name(), player2.get_symbol(), True)\
                        or check_columns(player2.get_player_name(), player2.get_symbol(), True)\
                        or check_diagonals(player2.get_player_name(), player2.get_symbol(), True):
                    return player2.winner()
                elif board1.draw():
                    player_details()
                    print("\n Tie")
                    return True
            else:
                print("Wrong input !")

play()