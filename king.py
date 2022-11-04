# class to represent a king

from chess_piece import ChessPiece
from queen import Queen

CHESS_DIMENSION = 8

class King(ChessPiece):
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_king'
        elif self.is_white == False:
            return 'black_king'

    # def is_valid_king_move(self, start_row, start_col, end_row, end_col):
    #     return Queen.is_valid_queen_move(self, start_row, start_col, end_row, end_col) and (abs(start_row - end_row) == 1 or abs(start_col - end_col) == 1)

    def get_valid_king_moves(self, chess_board, start_row, start_col):
        valid_king_moves = []
        # rook moves in 4 directions (up, down, left, right)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for x, y in directions:
            end_row = start_row + x
            end_col = start_col + y
            # no need for while loop since kings only move one square
            if 0 <= end_row < CHESS_DIMENSION and 0 <= end_col < CHESS_DIMENSION: 
                end_square = chess_board[end_row][end_col]
                end_square_color = self.is_piece_from_string(end_square)
                if end_square == ' ':
                    valid_king_moves.append((end_row, end_col))
                else:
                    if end_square_color != self.is_white:
                        valid_king_moves.append((end_row, end_col))

        return valid_king_moves
