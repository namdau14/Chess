# class to represent a player's move


from chess_game import ChessGame


class Move():
    def __init__(self, chess_board, start_square, end_square, is_castling = False):
        self.start_row = start_square[0] # the starting row of the moving piece
        self.start_col = start_square[1] # the col of the moving piece
        self.end_row = end_square[0] # the ending row of the moving piece
        self.end_col = end_square[1] # the ending col of the moving piece
        self.piece_moved = chess_board[self.start_row][self.start_col]
        # we are operating under the fact that every "square" can be captured, including empty squares (because piece or not it will be replaced by the "capturing" square)
        self.square_or_piece_captured = chess_board[self.end_row][self.end_col]
        self.is_castling = is_castling

    '''
    display the chess notation after a move
    '''
    def display_chess_notation(self, chess_board, letters_map, chess_dimension, game_move_log, move_array):
        row, col = move_array[1]
        notation_string = ''
        if 'rook' in chess_board[row][col]:
            notation_string += 'R'
        if 'knight' in chess_board[row][col]:
            notation_string += 'N'
        if 'bishop' in chess_board[row][col]:
            notation_string += 'B'
        if 'queen' in chess_board[row][col]:
            notation_string += 'Q'
        if 'king' in chess_board[row][col]:
            notation_string += 'K'
        notation_string += str(letters_map[col + 1]).lower() + str(chess_dimension - row)
        game_move_log.append(notation_string)
        return game_move_log

         
