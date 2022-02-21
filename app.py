import random

colomn_range = 3
blank = "-"

game_board = [
    [blank for i in range(colomn_range)],
    [blank for i in range(colomn_range)],
    [blank for i in range(colomn_range)]
]

def rules(num, symbol):
    cases = {
        1: game_board[0][0],
        2: game_board[0][1],
        3: game_board[0][2],
        4: game_board[1][0],
        5: game_board[1][1],
        6: game_board[1][2],
        7: game_board[2][0],
        8: game_board[2][1],
        9: game_board[2][2]
    }
    cases.get(num, "Invalid input")
    board_format(game_board)

def board_format(board):
    print("Tic Tac Toe")
    for row in board:
        print("{: >20} {: >20} {: >20}".format(*row))

#def play():

#board_format(game_board)

rules(int(input("enter a num: ")), "O")
