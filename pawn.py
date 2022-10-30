# class to represent a pawn


from chess_piece import ChessPiece


class Pawn(ChessPiece):
    def __init__(self, is_starting = True, is_en_passant = False, is_promoted = False):
        super().__init__(is_white = True)
        self.is_starting = is_starting
        self.is_en_passant = is_en_passant
        self.is_promoted = is_promoted

    def is_valid_pawn_move(self):
        if (self.is_valid_move()):
            return False
        
        
