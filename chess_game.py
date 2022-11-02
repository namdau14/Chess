# used to display the game state

CHESS_DIMENSION = 8

from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn

import pygame


class ChessGame():
    # default constructor
    def __init__(self):
        # initial board
        self.chess_board = [[' ' for i in range(CHESS_DIMENSION)] for j in range(CHESS_DIMENSION)]
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

    '''
    return list of valid moves (for hightlighting)
    '''

    def get_valid_moves(self, start_row, start_col):
        if self.chess_board[start_row][start_col] == 'white_rook':
            return self.white_rook.get_valid_rook_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'black_rook':
            return self.black_rook.get_valid_rook_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'white_knight':
            return self.white_knight.get_valid_knight_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'black_knight':
            return self.black_knight.get_valid_knight_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'white_bishop':
            return self.white_bishop.get_valid_bishop_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'black_bishop':
            return self.black_bishop.get_valid_bishop_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'white_queen':
            return self.white_queen.get_valid_queen_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'black_queen':
            return self.black_queen.get_valid_queen_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'white_king':
            return self.white_king.get_valid_king_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'black_king':
            return self.black_king.get_valid_king_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'white_pawn':
            return self.white_pawn.get_valid_pawn_moves(self.chess_board, start_row, start_col)
        elif self.chess_board[start_row][start_col] == 'black_pawn':
            return self.black_pawn.get_valid_pawn_moves(self.chess_board, start_row, start_col)
        else:
            return []
        
    """ 
    Make a move
    """
    def make_move(self, chess_board, move, letters_map, chess_dimension, game_move_log, move_array, valid_moves):

        if (move.end_row, move.end_col) in valid_moves:
            # set the beginning square to blank space
            self.chess_board[move.start_row][move.start_col] = ' '
            # set the moved square to the piece
            self.chess_board[move.end_row][move.end_col] = move.piece_moved
            # TODO: set piece captured to be removed from the game
            # log the move
            return move.display_chess_notation(chess_board, letters_map, chess_dimension, game_move_log, move_array)
        else:
            return []


# if __name__ == '__main__':
#     chess_game = ChessGame()
#     print(chess_game.initial_state())