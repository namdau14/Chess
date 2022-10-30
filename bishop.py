# class to represent a bishop


class Bishop():
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_bishop'
        elif self.is_white == False:
            return 'black_bishop'

    def is_valid_bishop_move(self, move, row, col):
        return abs(move.start_row - row) == abs(move.start_col - col)

    def get_valid_bishop_moves(self, move, chess_board):
        valid_bishop_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_bishop_move(move, row, col):
                    valid_bishop_moves.append((row, col))
        return valid_bishop_moves
