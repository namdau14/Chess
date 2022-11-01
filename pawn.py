# class to represent a pawn


class Pawn():
    def __init__(self, is_white = True, is_starting = True, is_en_passant = False, is_promoted = False):
        self.is_white = is_white
        self.is_starting = is_starting
        self.is_en_passant = is_en_passant
        self.is_promoted = is_promoted

    def get_text(self):
        if self.is_white == True:
            return 'white_pawn'
        elif self.is_white == False:
            return 'black_pawn'

    def is_valid_pawn_move(self, start_row, start_col, end_row, end_col):
        # if (self.is_starting == True):
        #     return (abs(move.start_col - col) == 1) or (abs(move.start_col - col) == 2)
            
        return (abs(start_row - end_row) == 1)
        
        
    def get_valid_pawn_moves(self, chess_board, start_row, start_col):
        valid_pawn_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_pawn_move(start_row, start_col, row, col) and not (start_row == row and start_col == col):
                    valid_pawn_moves.append((row, col))
        return valid_pawn_moves