# class to represent a king

from chess_piece import ChessPiece
from queen import Queen

class King(ChessPiece):
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_king'
        elif self.is_white == False:
            return 'black_king'

    def is_valid_king_move(self, start_row, start_col, end_row, end_col):
        return Queen.is_valid_queen_move(self, start_row, start_col, end_row, end_col) and (abs(start_row - end_row) == 1 or abs(start_col - end_col) == 1)

    def get_valid_king_moves(self, chess_board, start_row, start_col):
        valid_king_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_king_move(start_row, start_col, row, col) and not (start_row == row and start_col == col):
                    valid_king_moves.append((row, col))
        return valid_king_moves
