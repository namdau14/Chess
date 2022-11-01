# class to represent a rook


class Rook():
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_rook'
        elif self.is_white == False:
            return 'black_rook'

    def is_valid_rook_move(self, move, row, col):
        return move.start_row == row or move.start_col == col

    # probably need a dfs algorithm here

    def get_valid_rook_moves(self, move, chess_board):
        valid_rook_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_rook_move(move, row, col):
                    valid_rook_moves.append((row, col))
        return valid_rook_moves


        