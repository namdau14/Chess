# Generic class representing a chess piece, which will contain methods that all pieces in Chess share (unable to move with same side block,...)

# map to connect pieces to their string representation

CHESS_DIMENSION = 8

class ChessPiece(object):
    def __init__(self, is_white):
        self.is_white = is_white
    
    '''
    Get piece color from string
    '''
    def is_piece_from_string(self, string):
        if 'white' in string:
            return True
        elif 'black' in string:
            return False

