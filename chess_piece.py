# Generic class representing a chess piece, which will contain methods that all pieces in Chess share (unable to move with same side block,...)

class ChessPiece(object):
    def __init__(self, is_white):
        self.is_white = is_white
    
    '''
    All pieces share the same distinction of unable to move while another piece of same color is blocking the square
    '''
    def is_valid_move(self, chess_piece):
        if chess_piece.is_white == self.is_white:
            return False

