# class to represent a queen

from rook import Rook
from bishop import Bishop

class Queen():
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_queen'
        elif self.is_white == False:
            return 'black_queen'

    def is_valid_queen_move(self, move, row, col):
        return Rook.is_valid_rook_move(self, move, row, col) or Bishop.is_valid_bishop_move(self, move, row, col)

    def get_valid_queen_moves(self, move, chess_board):
        valid_queen_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_queen_move(move, row, col):
                    valid_queen_moves.append((row, col))
        return valid_queen_moves
