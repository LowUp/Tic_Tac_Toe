#Player class
class Player:

    def __init__(self, board, player_name):
        self.player_name = player_name
        self.board = board

    def game_board(self):
        return self.board

    def set_board(self, num, symbol):
        if num == 7:
            self.game_board()[0][0] = symbol
            print("You played at position (1,1)")
        elif num == 8:
            self.game_board()[0][1] = symbol
            print("You played at position (1,2)")
        elif num == 9:
            self.game_board()[0][2] = symbol
            print("You played at position (1,3)")
        elif num == 4:
            self.game_board()[1][0] = symbol
            print("You played at position (2,1)")
        elif num == 5:
            self.game_board()[1][1] = symbol
            print("You played at position (2,2)")
        elif num == 6:
            self.game_board()[1][2] = symbol
            print("You played at position (2,3)")
        elif num == 1:
            self.game_board()[2][0] = symbol
            print("You played at position (3,1)")
        elif num == 2:
            self.game_board()[2][1] = symbol
            print("You played at position (3,2)")
        elif num == 3:
            self.game_board()[2][2] = symbol
            print("You played at position (3,3)")
        else:
            print("Invalid input")

    def get_player_name(self):
        return f"{self.player_name}"


# AI player class
class ComputerPlayer(Player):
    def __init__(self, board, player_name):
        super().__init__(board, player_name)

    def set_board(self, num, symbol):
        if num == 7:
            self.game_board()[0][0] = symbol
            print("The AI played at position (1,1)")
        elif num == 8:
            self.game_board()[0][1] = symbol
            print("The AI played at position (1,2)")
        elif num == 9:
            self.game_board()[0][2] = symbol
            print("The AI played at position (1,3)")
        elif num == 4:
            self.game_board()[1][0] = symbol
            print("The AI played at position (2,1)")
        elif num == 5:
            self.game_board()[1][1] = symbol
            print("The AI played at position (2,2)")
        elif num == 6:
            self.game_board()[1][2] = symbol
            print("The AI played at position (2,3)")
        elif num == 1:
            self.game_board()[2][0] = symbol
            print("The AI played at position (3,1)")
        elif num == 2:
            self.game_board()[2][1] = symbol
            print("The AI played at position (3,2)")
        elif num == 3:
            self.game_board()[2][2] = symbol
            print("The AI played at position (3,3)")
        else:
            print("Invalid input")

    @staticmethod
    def getPossibleMoves():
        possible_moves = [i + 1 for i in range(9)]  # List of moves the AI will be able to do.
        return possible_moves

    def deleteMove(self, num):
        self.getPossibleMoves().remove(num)

# Game class
class Game:

    def __init__(self):
        self.board = [
            ["-" for i in range(3)],
            ["-" for i in range(3)],
            ["-" for i in range(3)]
        ]

    def game_board(self):
        return self.board

    @staticmethod
    def ref_board():
        ref_board = [
            [7 + i for i in range(3)],
            [4 + i for i in range(3)],
            [1 + i for i in range(3)]]
        return ref_board

    def get_board(self):
        print("Tic Tac Toe")
        for row in self.board:
            print("{: >20} {: >20} {: >20}".format(*row))

    def get_refBoard(self):
        print("Reference board")
        for row in self.ref_board():
            print("{: >20} {: >20} {: >20}".format(*row))

    def get_row(self, num):
        return self.game_board()[num]

    def get_column(self, num):
        column = [self.game_board()[0][num], self.game_board()[1][num], self.game_board()[2][num]]
        return column

    def get_diagonal(self, num):
        if num == 0:
            diagonal = [self.game_board()[0][0], self.game_board()[1][1], self.game_board()[2][2]]
            return diagonal
        elif num == 1:
            diagonal = [self.game_board()[0][2], self.game_board()[1][1], self.game_board()[2][0]]
            return diagonal

