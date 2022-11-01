# used to display the game state

CHESS_DIMENSION = 8

from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn


class ChessGame():
    # default constructor
    def __init__(self):
        # initial board
        self.chess_board = [[' ' for i in range(8)] for j in range(8)]
        # flag to represent if white is moving
        self.is_white = True
        # array to represent the list of moves that has been played
        self.move_list = []

        # pieces representation
        self.white_rook = Rook(is_white = True)
        self.black_rook = Rook(is_white = False)
        self.white_knight = Knight(is_white = True)
        self.black_knight = Knight(is_white = False)
        self.white_bishop = Bishop(is_white = True)
        self.black_bishop = Bishop(is_white = False)
        self.white_queen = Queen(is_white = True)
        self.black_queen = Queen(is_white = False)
        self.white_king = King(is_white = True)
        self.black_king = King(is_white = False)
        self.white_pawn = Pawn(is_white = True)
        self.black_pawn = Pawn(is_white = False)


    
    """ 
    Put pieces in the initial 
    positions of the game 
    """
    def initial_state(self):
        black_pieces = [self.black_rook.get_text(), self.black_knight.get_text(), self.black_bishop.get_text(), self.black_queen.get_text(), self.black_king.get_text()]
        white_pieces = [self.white_rook.get_text(), self.white_knight.get_text(), self.white_bishop.get_text(), self.white_queen.get_text(), self.white_king.get_text()]
        # place black pieces
        self.chess_board[0][0:5] = black_pieces[0:5]
        self.chess_board[0][5:8] = black_pieces[0:3][::-1]
        # place black pawns
        self.chess_board[1] = [self.black_pawn.get_text()] * CHESS_DIMENSION
        # place white pieces
        self.chess_board[7][0:5] = white_pieces[0:5]
        self.chess_board[7][5:8] = white_pieces[0:3][::-1]
        # place white pawns
        self.chess_board[6] = [self.white_pawn.get_text()] * CHESS_DIMENSION
        return self.chess_board
        
    """ 
    Make a move
    """
    def make_move(self, move, letters_map, chess_dimension, game_move_log, move_array):
        valid_moves = []
        if self.chess_board[move.start_row][move.start_col] == 'white_rook':
            valid_moves = self.white_rook.get_valid_rook_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'black_rook':
            valid_moves = self.black_rook.get_valid_rook_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'white_knight':
            valid_moves = self.white_knight.get_valid_knight_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'black_knight':
            valid_moves = self.black_knight.get_valid_knight_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'white_bishop':
            valid_moves = self.white_bishop.get_valid_bishop_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'black_bishop':
            valid_moves = self.black_bishop.get_valid_bishop_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'white_queen':
            valid_moves = self.white_queen.get_valid_queen_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'black_queen':
            valid_moves = self.black_queen.get_valid_queen_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'white_king':
            valid_moves = self.white_king.get_valid_king_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'black_king':
            valid_moves = self.black_king.get_valid_king_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'white_pawn':
            valid_moves = self.white_pawn.get_valid_pawn_moves(move, self.chess_board)
        elif self.chess_board[move.start_row][move.start_col] == 'black_pawn':
            valid_moves = self.black_pawn.get_valid_pawn_moves(move, self.chess_board)

        if (move.end_row, move.end_col) in valid_moves:
            # set the beginning square to blank space
            self.chess_board[move.start_row][move.start_col] = ' '
            # set the moved square to the piece
            self.chess_board[move.end_row][move.end_col] = move.piece_moved
            # TODO: set piece captured to be removed from the game
            # log the move
            return move.display_chess_notation(letters_map, chess_dimension, game_move_log, move_array)


# if __name__ == '__main__':
#     chess_game = ChessGame()
#     print(chess_game.initial_state())