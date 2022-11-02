# class to represent a bishop

CHESS_DIMENSION = 8
from chess_piece import ChessPiece


class Bishop(ChessPiece):
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_bishop'
        elif self.is_white == False:
            return 'black_bishop'

    # def is_valid_bishop_move(self, start_row, start_col, end_row, end_col):
    #     return abs(start_row - end_row) == abs(start_col - end_col)

    def get_valid_bishop_moves(self, chess_board, start_row, start_col):
        valid_bishop_moves = []
        # bishop moves in 4 diagonal directions
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for x, y in directions:
            end_row = start_row + x
            end_col = start_col + y
            while 0 <= end_row < CHESS_DIMENSION and 0 <= end_col < CHESS_DIMENSION: 
                end_square = chess_board[end_row][end_col]
                end_square_color = self.is_piece_from_string(end_square)
                if end_square == ' ':
                    valid_bishop_moves.append((end_row, end_col))
                    end_row += x
                    end_col += y
                else:
                    if end_square_color != self.is_white:
                        valid_bishop_moves.append((end_row, end_col))
                        break
                    elif end_square_color == self.is_white:
                        break
        return valid_bishop_moves