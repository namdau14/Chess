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

    def is_valid_pawn_move(self, move, row, col):
        # if (self.is_starting == True):
        #     return (abs(move.start_col - col) == 1) or (abs(move.start_col - col) == 2)
            
        return (abs(move.start_row - row) == 1)
        
        
    def get_valid_pawn_moves(self, move, chess_board):
        valid_pawn_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_pawn_move(move, row, col):
                    valid_pawn_moves.append((row, col))
        return valid_pawn_moves