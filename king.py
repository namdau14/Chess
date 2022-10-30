# class to represent a king

from queen import Queen

class King():
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_king'
        elif self.is_white == False:
            return 'black_king'

    def is_valid_king_move(self, move, row, col):
        return Queen.is_valid_queen_move(self, move, row, col) and (abs(move.start_row - row) == 1 or abs(move.start_col - col) == 1)

    def get_valid_king_moves(self, move, chess_board):
        valid_king_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_king_move(move, row, col):
                    valid_king_moves.append((row, col))
        return valid_king_moves