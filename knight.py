# class to represent a knight

class Knight():
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_knight'
        elif self.is_white == False:
            return 'black_knight'

    def is_valid_knight_move(self, move, row, col):
        return abs(move.start_row - row) * abs(move.start_col - col) == 2

    def get_valid_knight_moves(self, move, chess_board):
        valid_knight_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_knight_move(move, row, col):
                    valid_knight_moves.append((row, col))
        return valid_knight_moves

