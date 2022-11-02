# class to represent a knight

from chess_piece import ChessPiece


class Knight(ChessPiece):
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_knight'
        elif self.is_white == False:
            return 'black_knight'

    def is_valid_knight_move(self, chess_board, start_row, start_col, end_row, end_col):
        end_square_string = chess_board[end_row][end_col]
        end_square_color = self.is_piece_from_string(end_square_string)
        if end_square_string != ' ':
            if end_square_color == self.is_white:
                return False
        return abs(start_row - end_row) * abs(start_col - end_col) == 2

    def get_valid_knight_moves(self, chess_board, start_row, start_col):
        valid_knight_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_knight_move(chess_board, start_row, start_col, row, col) and not (start_row == row and start_col == col):
                    valid_knight_moves.append((row, col))
        return valid_knight_moves


