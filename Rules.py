class Rules:

    def __init__(self, game_board, player_number):
        self.game_board = game_board
        self.player_number = player_number

    def get_board(self):
        for row in self.game_board:
            print("{: >20} {: >20} {: >20}".format(*row))

    def set_board(self, num, symbol):
        if num == 7:
            self.game_board[0][0] = symbol
            print("You played at position (1,1)")
        elif num == 8:
            self.game_board[0][1] = symbol
            print("You played at position (1,2)")
        elif num == 9:
            self.game_board[0][2] = symbol
            print("You played at position (1,3)")
        elif num == 4:
            self.game_board[1][0] = symbol
            print("You played at position (2,1)")
        elif num == 5:
            self.game_board[1][1] = symbol
            print("You played at position (2,2)")
        elif num == 6:
            self.game_board[1][2] = symbol
            print("You played at position (2,3)")
        elif num == 1:
            self.game_board[2][0] = symbol
            print("You played at position (3,1)")
        elif num == 2:
            self.game_board[2][1] = symbol
            print("You played at position (3,2)")
        elif num == 3:
            self.game_board[2][2] = symbol
            print("You played at position (3,3)")
        else:
            print("Invalid input")

    def get_row(self, num):
        return self.game_board[num]

    def get_column(self, num):
        column = [self.game_board[0][num], self.game_board[1][num], self.game_board[2][num]]
        return column

    def get_diagonal(self, num):
        if num == 0:
            diagonal = [self.game_board[0][0], self.game_board[1][1], self.game_board[2][2]]
            return diagonal
        elif num == 1:
            diagonal = [self.game_board[0][2], self.game_board[1][1], self.game_board[2][0]]
            return diagonal

    def get_player_name(self):
        return f"player {self.player_number}"
