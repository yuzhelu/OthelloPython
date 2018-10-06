
class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board:

    def __init__(self):
        self.__rows = 8
        self.__col = 8
        self.__gameBoard = [['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_'],
                          ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_'],
                          ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_']]

        self.__gameBoard[3][3] = 'W'
        self.__gameBoard[4][4] = 'W'
        self.__gameBoard[3][4] = 'B'
        self.__gameBoard[4][3] = 'B'

        self.__white_score = 0
        self.__black_score = 0
        self.__remaining = 1        # just anything but zero

    def get_white_score(self):
        return self.__white_score

    def get_black_score(self):
        return self.__black_score

    def print_game_board(self):

        column_X = ["           ", 0, 1, 2, 3, 4, 5, 6, 7]
        column_horizontal = '='
        row_vertical = '|'

        # prints column and row header numbers
        print("             Columns")
        for elem in column_X:
            print(str(elem), end=" ")
        print()

        print("            ", end="")

        for i in range(self.__col):
            print(column_horizontal, end=" ")
        print()

        # print grind and element values
        j = 0  # row
        k = 0  # col
        for j in range(self.__rows):
            if j == 3:
                print("Rows     " + str(j) + row_vertical + " ", end="")

            else:
                print("         " + str(j) + row_vertical + " ", end="")

            for k in range(self.__col):
                print(str(self.__gameBoard[j][k]), end=" ")
            print()

    def find_valid_points(self, player, opponent, available_points):
        for i in range(self.__rows):
            for j in range(self.__col):
                if self.__gameBoard[i][j] == opponent:
                    I = i
                    J = j
                    if i - 1 >= 0 and self.__gameBoard[i-1][j] == '_':
                        i = i + 1
                        while i < 7 and self.__gameBoard[i][j] == opponent:
                            i += 1
                        if i <= 7 and self.__gameBoard[i][j] == player:
                            available_points.add(Piece(I -1, J))

                    i = I
                    j = J
                    if i + 1 <= 7 and self.__gameBoard[i + 1][j] == '_':
                        i = i - 1
                        while i < 7 and self.__gameBoard[i][j] == opponent:
                            i -= 1
                        if i >= 0 and self.__gameBoard[i][j] == player:
                            available_points.add(Piece(I + 1, J))

                    i = I
                    j = J
                    if j - 1 >= 0 and self.__gameBoard[i][j-1] == '_':
                        j += 1
                        while j < 7 and self.__gameBoard[i][j] == opponent:
                            j += 1
                        if j <= 7 and self.__gameBoard[i][j] == player:
                            available_points.add(Piece(I, J - 1))

                    i = I
                    j = J
                    if j + 1 <= 7 and self.__gameBoard[i][j+1] == '_':
                        j -= 1
                        while j > 0 and self.__gameBoard[i][j] == opponent:
                            j -= 1
                        if j >= 0 and self.__gameBoard[i][j] == player:
                            available_points.add(Piece(I, J + 1))
                    i = I
                    j = J

    def get_valid_points(self, player, opponent):
        available_points = set()
        self.find_valid_points(player, opponent, available_points)
        return available_points

    def display_valid_spots(self, available_points, player, opponent):

        for cell in available_points:
            x = cell.x
            y = cell.y

            self.__gameBoard[x][y] = '*'
        self.print_game_board()
        for cell in available_points:
            x = cell.x
            y = cell.y
            self.__gameBoard[x][y] = '_'    # resets the point

    def move_result(self, white_valid_spots, black_valid_spots):
        self.update_scores()

        if not white_valid_spots and not black_valid_spots or self.__remaining == 0:   # white and avail is empty
            if len(white_valid_spots) > len(black_valid_spots):
                return 1
            if len(black_valid_spots) > len(white_valid_spots):
                return -1
            else:
                return 0

        if self.__white_score == 0 or self.__black_score == 0:
            if self.__white_score > self.__black_score:
                return 1
            if self.__white_score < self.__black_score:
                return -1
            else:
                return 0
        return 9    # default return

    def update_scores(self):
        self.__white_score = 0
        self.__black_score = 0
        self.__remaining = 0

        for i in range(self.__rows):
            for j in range(self.__col):
                if self.__gameBoard[i][j] == 'W':
                    self.__white_score += 1
                elif self.__gameBoard[i][j] == 'B':
                    self.__black_score += 1
                else:
                    self.__remaining += 1

    def input_move(self, cell, player, opponent):
        i = cell.x
        j = cell.y
        I = i
        J = j

        self.__gameBoard[i][j] = player

        # checks left for opponent
        if i - 1 >= 0 and self.__gameBoard[i-1][j] == opponent:
            i -= 1
            while i > 0 and self.__gameBoard[i][j] == opponent:
                i -= 1
            if i >= 0 and self.__gameBoard[i][j] == player:
                while i != I - 1:
                    i += 1
                    self.__gameBoard[i][j] = player
        # checks right for opponent
        i = I
        j = J
        if i + 1 <= 7 and self.__gameBoard[i+1][j] == opponent:
            i += 1
            while i < 7 and self.__gameBoard[i][j] == opponent:
                i += 1
            if i <= 7 and self.__gameBoard[i][j] == player:
                while i != I + 1:
                    i -= 1
                    self.__gameBoard[i][j] = player
        # checks top for opponent
        i = I
        j = J
        if j - 1 >= 0 and self.__gameBoard[i][j - 1] == opponent:
            j -= 1
            while j > 0 and self.__gameBoard[i][j] == opponent:
                j -= 1
            if j >= 0 and self.__gameBoard[i][j] == player:
                while j != J - 1:
                    j += 1
                    self.__gameBoard[i][j] = player

        # checks bottom for opponent
        i = I
        j = J
        if j + 1 <= 7 and self.__gameBoard[i][j+1] == opponent:
            j += 1
            while j < 7 and self.__gameBoard[i][j] == opponent:
                j += 1
            if j >= 7 and self.__gameBoard[i][j] == player:
                while j != J + 1:
                    j -= 1
                    self.__gameBoard[i][j] = player

# im using the cantor pairing function to hash
def hashInteger(self, x, y):

    hashValue = (x + y) * (x + y + 1) / (2 + x)

    return hashValue



