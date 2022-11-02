# class to represent a bishop


from chess_piece import ChessPiece


class Bishop(ChessPiece):
    def __init__(self, is_white = True):
        self.is_white = is_white

    def get_text(self):
        if self.is_white == True:
            return 'white_bishop'
        elif self.is_white == False:
            return 'black_bishop'

    def is_valid_bishop_move(self, start_row, start_col, end_row, end_col):
        return abs(start_row - end_row) == abs(start_col - end_col)

    def get_valid_bishop_moves(self, chess_board, start_row, start_col):
        valid_bishop_moves = []
        for row in range(len(chess_board)):
            for col in range(len(chess_board)):
                if self.is_valid_bishop_move(start_row, start_col, row, col) and not (start_row == row and start_col == col):
                    valid_bishop_moves.append((row, col))
        return valid_bishop_moves
