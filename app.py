import time

from Rules import Player
from Rules import ComputerPlayer
from Rules import UnbeatableAI
from Rules import Game

board = Game()

game_board = board.game_board()

player1 = Player(game_board, input("Player 1 enter your username: ").upper())

playerTest = UnbeatableAI(game_board, "AItest")

# Decides if player 2 will be an AI or a human player
player2_username = input("Player 2 enter your username: ").upper()

if player2_username == "AI":
    player2 = ComputerPlayer(game_board, player2_username)
else:
    player2 = Player(game_board, player2_username)


def player_details():
    board.get_refBoard()
    board.get_board()


def check_rows(playerName, playerSymbol):
    rows_number = 3
    win = f'{playerSymbol}{playerSymbol}{playerSymbol}'

    for i in range(rows_number):
        row = ''.join(board.get_row(i))
        if row == win:
            board.get_board()
            print(f"\n{playerName} wins")
            return True


def check_columns(playerName, playerSymbol):
    columns_number = 3
    win = f'{playerSymbol}{playerSymbol}{playerSymbol}'

    for i in range(columns_number):
        column = ''.join(board.get_column(i))
        if column == win:
            board.get_board()
            print(f"\n{playerName} wins")
            return True


def check_diagonals(playerName, playerSymbol):

    diagonals_number = 2
    win = f'{playerSymbol}{playerSymbol}{playerSymbol}'

    for i in range(diagonals_number):
        diagonal = ''.join(board.get_diagonal(i))
        if diagonal == win:
            board.get_board()
            print(f"\n{playerName} wins")
            return True

# def hard_ai (symbol):
#    bestScore = -1000
#    bestMove = 0

#    for key in game_board:
#        if(game_board[key] == "-"):
#            game_board[key] = symbol
#            score = minimax(game_board,0,False)
#            game_board[key] = "-"
#            if(score > bestScore):
#                bestScore = score
#                bestMove = key

#    return playerTest.get_move(bestMove)

# def minimax(board, depth, isMaximizing):

   # if check_rows(player1.get_player_name(), player1_symbol.upper()) \
   #         or check_columns(player1.get_player_name(), player1_symbol.upper()) \
   #         or check_diagonals(player1.get_player_name(), player1_symbol.upper()):


def play():

    # Players choose symbols (X or O)
    played_position = ["" for i in range(9)]
    counter = 0

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

            elif player1_input in range(1,10):
                if player2_username == "AI":
                    player2.deleteMove(player1_input)
                flag1 = False
                player1.set_board(player1_input, player1.get_symbol())
                played_position[counter] = player1_input
                counter += 1
                print(f"played position {played_position}")

                # Checks if the player wins the game or if tie
                if check_rows(player1.get_player_name(), player1.get_symbol()) \
                        or check_columns(player1.get_player_name(), player1.get_symbol())\
                        or check_diagonals(player1.get_player_name(), player1.get_symbol()):
                    return player1.winner()
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
                player2_input = player2.get_move()
            else:
                try:
                    player2_input = int(input(f"{player2.get_player_name()} choose a position from 1 to 9: "))
                except ValueError:
                    print("Wrong input")

            if player2_input in played_position:
                print("This position has already been played\nRetry")

            elif player2_input in range(1,10):
                if player2_username == "AI":
                    player2.deleteMove(player2_input)
                    time.sleep(0.5)
                flag2 = False
                player2.set_board(player2_input, player2.get_symbol())
                played_position[counter] = player2_input
                counter += 1
                print(f"played position {played_position}")

                # Checks if the player wins the game or if tie
                if check_rows(player2.get_player_name(), player2.get_symbol())\
                        or check_columns(player2.get_player_name(), player2.get_symbol())\
                        or check_diagonals(player2.get_player_name(), player2.get_symbol()):
                    return player2.winner()
                elif counter >= 9:
                    player_details()
                    print("\n Tie")
                    return True
            else:
                print("Wrong input !")

play()