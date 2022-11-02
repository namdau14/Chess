# class to represent a rook

CHESS_DIMENSION = 8

from chess_piece import ChessPiece

class Rook(ChessPiece):
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_rook'
        elif self.is_white == False:
            return 'black_rook'

    # def is_valid_rook_move(self, start_row, start_col, end_row, end_col):
    #     return start_row == end_row or start_col == end_col

    def get_valid_rook_moves(self, chess_board, start_row, start_col):
        valid_rook_moves = []
        # rook moves in 4 directions (up, down, left, right)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x, y in directions:
            end_row = start_row + x
            end_col = start_col + y
            while 0 <= end_row < CHESS_DIMENSION and 0 <= end_col < CHESS_DIMENSION: 
                end_square = chess_board[end_row][end_col]
                end_square_color = self.is_piece_from_string(end_square)
                if end_square == ' ':
                    valid_rook_moves.append((end_row, end_col))
                    end_row += x
                    end_col += y
                else:
                    if end_square_color != self.is_white:
                        valid_rook_moves.append((end_row, end_col))
                        break
                    elif end_square_color == self.is_white:
                        break
        return valid_rook_moves


        