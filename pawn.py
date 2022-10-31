# class to represent a pawn


class Pawn():
    def __init__(self, is_white = True, is_starting = True, is_en_passant = False, is_promoted = False):
        self.is_white = is_white
        self.is_starting = is_starting
        self.is_en_passant = is_en_passant
        self.is_promoted = is_promoted

    def is_valid_pawn_move(self):
        
        
        
