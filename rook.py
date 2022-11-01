# class to represent a rook


class Rook():
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_rook'
        elif self.is_white == False:
            return 'black_rook'

    def is_valid_rook_move(self, start_row, start_col, end_row, end_col):
        return start_row == end_row or start_col == end_col

    # probably need a dfs algorithm here

    def get_valid_rook_moves(self, chess_board, start_row, start_col):
        valid_rook_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_rook_move(start_row, start_col, row, col) and not (start_row == row and start_col == col):
                    valid_rook_moves.append((row, col))
        return valid_rook_moves


        