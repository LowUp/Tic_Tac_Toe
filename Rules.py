class Rules:

    def __init__(self, game_board):
        self.game_board = game_board

    def get_board(self):
        print("Tic Tac Toe")
        for row in self.game_board:
            print("{: >20} {: >20} {: >20}".format(*row))

    def set_board(self, num, symbol):
        if num == 1:
            self.game_board[0][0] = symbol
            print("You played at position (0,0)")
        elif num == 2:
            self.game_board[0][1] = symbol
            print("You played at position (0,1)")
        elif num == 3:
            self.game_board[0][2] = symbol
            print("You played at position (0,2)")
        elif num == 4:
            self.game_board[1][0] = symbol
            print("You played at position (1,0)")
        elif num == 5:
            self.game_board[1][1] = symbol
            print("You played at position (1,1)")
        elif num == 6:
            self.game_board[1][2] = symbol
            print("You played at position (1,2)")
        elif num == 7:
            self.game_board[2][0] = symbol
            print("You played at position (2,0)")
        elif num == 8:
            self.game_board[2][1] = symbol
            print("You played at position (2,1)")
        elif num == 9:
            self.game_board[2][2] = symbol
            print("You played at position (2,2)")
        else:
            print("Invalid input")

