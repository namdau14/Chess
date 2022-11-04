# class to represent a pawn


from chess_piece import ChessPiece
CHESS_DIMENSION = 8


class Pawn(ChessPiece):
    def __init__(self, is_white, is_en_passant = False, is_promoted = False):
        self.is_white = is_white
        self.is_en_passant = is_en_passant
        self.is_promoted = is_promoted

    def get_text(self):
        if self.is_white == True:
            return 'white_pawn'
        elif self.is_white == False:
            return 'black_pawn'

    def is_valid_white_pawn_move(self, start_row, start_col, end_row, end_col, initial_row = 6):
        if (start_row == initial_row):
                return ((start_row - end_row == 1) or (start_row - end_row == 2)) and start_col == end_col
        return (start_row - end_row == 1) and start_col == end_col

    def is_valid_black_pawn_move(self, start_row, start_col, end_row, end_col, initial_row = 1):
        if (start_row == initial_row):
                return ((end_row - start_row == 1) or (end_row - start_row == 2)) and start_col == end_col
        return (end_row - start_row == 1) and start_col == end_col
        
        
    def get_valid_pawn_moves(self, chess_board, start_row, start_col):
        valid_pawn_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if 'white' in chess_board[start_row][start_col]:
                    if self.is_valid_white_pawn_move(start_row, start_col, row, col) and not (start_row == row and start_col == col):
                        valid_pawn_moves.append((row, col))
                if 'black' in chess_board[start_row][start_col]:
                    if self.is_valid_black_pawn_move(start_row, start_col, row, col) and not (start_row == row and start_col == col):
                        valid_pawn_moves.append((row, col))
        return valid_pawn_moves