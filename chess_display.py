# used to display the game


# TODO Get new images for the chess pieces. display moveset array on GUI. Start implementing rules for pawn and king (castling). Start looking in to checks and checkmate


from chess_game import ChessGame
import pygame
from pygame.locals import * # import commands such as QUIT, MOUSEBUTTONDOWN,...
from move import Move

# dimension of actual board
BOARD_DIMENSION = 1000

# chess board size(8 x 8)
CHESS_DIMENSION = 8

# set piece_size length
PIECE_SIZE = BOARD_DIMENSION / CHESS_DIMENSION 

# set GUI length

BACKGROUND_WIDTH = BOARD_DIMENSION + 300
BACKGROUND_HEIGHT = BOARD_DIMENSION + 200

# index to center the board

CENTER_INDEX = (BACKGROUND_HEIGHT - BOARD_DIMENSION) / 2

# map to map each piece name with its corresponding image (so that when a piece moves we modify the letters instead of the image)
TEXT_TO_IMAGE = {}

# map letters to number for chess notation
LETTERS_MAP = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: "F", 7: "G", 8: "H"}

class ChessDisplay():

    '''
    where the main game driver is located
    '''

    def main(self):

        # initialize pygame
        pygame.init()

        # set game screen dimension
        board_screen = self.resize_window(BACKGROUND_WIDTH, BACKGROUND_HEIGHT)
        pygame.display.set_caption("It's Chessin Time")

        # call the chess game and set it to the initial state
        chess_game = ChessGame()
        chess_game.initial_state()
        
        # load the images corresponding to the pieces
        self.load_piece_images()

        # dynamic array to keep track of 1 move
        move_array = []

        # array to keep track of every move in the game
        game_move_log = []

        # array to keep track of valid moves of a piece

        valid_moves = []

        # numbers to keep track of the clicked row and col (set to negative infinity first to avoid being mistaken for a game square)

        clicked_row, clicked_col  = -float('inf'), -float('inf')

        # run the game
        run = True
        while run:
            for event in pygame.event.get():
                # quit the game
                if event.type == QUIT:
                    run = False
                # allow for full screen mode
                if event.type == VIDEORESIZE:
                    board_screen = self.resize_window(event.w, event.h)
                if event.type == MOUSEBUTTONDOWN:
                    # condition so that it only works when you click the left mouse button
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_col, mouse_row = mouse_pos[0], mouse_pos[1]
                    
                        # perform actions only if it is within the chess board boundaries
                        if (CENTER_INDEX <= mouse_col <= CENTER_INDEX + BOARD_DIMENSION and CENTER_INDEX <= mouse_row <= CENTER_INDEX + BOARD_DIMENSION):
                            clicked_col = int((mouse_col - CENTER_INDEX) // PIECE_SIZE)
                            clicked_row = int((mouse_row - CENTER_INDEX) // PIECE_SIZE)
                            # save a move array to use for chess notation and to limit clicks
                            move_array.append((clicked_row, clicked_col))

                            if len(move_array) == 1:
                                valid_moves = chess_game.get_valid_moves(clicked_row, clicked_col)
                                # if clicked on empty square, reset click
                                if (chess_game.chess_board[clicked_row][clicked_col] == ' '):
                                    move_array = [] 
                                
                            if len(move_array) == 2:
                                move = Move(chess_game.chess_board, move_array[0], move_array[1])
                                game_move_log = chess_game.make_move(chess_game.chess_board, move, LETTERS_MAP, CHESS_DIMENSION, game_move_log, move_array, valid_moves)
                                print(game_move_log)
                                # reset move array and valid moves to continue with next move
                                move_array = []              
                                valid_moves = []

  
            # while game is running, display the current state of the game
            self.display_current_state(board_screen, chess_game, valid_moves, clicked_row, clicked_col, move_array) 
            pygame.display.flip()

    '''
    helper method to resize the window
    '''

    def resize_window(self, width, height):
        # set new game screen dimension
        board_screen = pygame.display.set_mode((width, height),
                                              pygame.RESIZABLE)
        # set background
        background = pygame.Surface(board_screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        board_screen.blit(background, (0, 0))
        return board_screen

    '''
    load the image to the corresponding piece
    '''

    def load_piece_images(self):
        chess_pieces = ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_pawn', 'white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_pawn']
        for chess_piece in chess_pieces:
            # scale chess images to be the correct size
            image = pygame.image.load('Chess_Pieces_Images/' + chess_piece + '.png')
            image_scale = pygame.transform.scale(image, (PIECE_SIZE, PIECE_SIZE))
            TEXT_TO_IMAGE[chess_piece] = image_scale

        


    '''
    display the current state of the game
    '''

    def display_current_state(self, board_screen, chess_game, valid_moves, clicked_row, clicked_col, move_array):
        self.display_board(board_screen, chess_game, valid_moves)
        self.display_pieces(board_screen, chess_game, clicked_row, clicked_col, move_array)
        self.display_moveset_box(board_screen)

    '''
    display the chess board
    '''
    def display_board(self, board_screen, chess_game, valid_moves):
        # light squares are placed where row num + col num = even number (zero index)
        # dark squares are placed where row num + col num = odd number (zero index)

        for row in range(CHESS_DIMENSION):
            for col in range(CHESS_DIMENSION):
                surface = pygame.Surface((PIECE_SIZE, PIECE_SIZE))

                if ((row + col) % 2 == 0):
                    surface.fill((177, 228, 185))
                elif ((row + col) % 2 == 1):
                    surface.fill((112, 162, 163))
                
                # color the valid moves square

                if (row, col) in valid_moves:
                    # if the square is not empty, draw a bigger circle without filling to easily identify
                    if chess_game.chess_board[row][col] != ' ':
                        pygame.draw.circle(surface, color = pygame.Color(255,100,100), center = (PIECE_SIZE / 2, PIECE_SIZE / 2), radius = PIECE_SIZE / 2, width = 4)
                    # else, draw smaller circle with filling
                    else:
                        pygame.draw.circle(surface, color = pygame.Color(255,100,100), center = (PIECE_SIZE / 2, PIECE_SIZE / 2), radius = PIECE_SIZE / 8)
                # multiply with row and col so that the sqaures fit in the correct index
                board_screen.blit(surface, (CENTER_INDEX + col * PIECE_SIZE, CENTER_INDEX + row * PIECE_SIZE))

    '''
    display the chess pieces and the leters/number designation
    '''
    def display_pieces(self, board_screen, chess_game, clicked_row, clicked_col, move_array):

        highlight_surface = pygame.Surface((PIECE_SIZE, PIECE_SIZE))

        for row in range(CHESS_DIMENSION):
            for col in range(CHESS_DIMENSION):
                piece = chess_game.chess_board[row][col]
                if piece != ' ':
                    # if user click on a piece to move it, highlight the square under that piece
                    if row == clicked_row and col == clicked_col and len(move_array) == 1:
                        highlight_surface.fill((255, 255, 0))
                        board_screen.blit(highlight_surface, (CENTER_INDEX + col * PIECE_SIZE, CENTER_INDEX + row * PIECE_SIZE))

                    # fill non-empty sqaure with their corresponding piece
                    board_screen.blit(TEXT_TO_IMAGE[piece], (CENTER_INDEX + col * PIECE_SIZE, CENTER_INDEX + row * PIECE_SIZE))
                # place the letters in their respective row
                if row == 7:
                    font = pygame.font.SysFont(name = 'Calibri', size = 50)
                    text = font.render(str(LETTERS_MAP[col + 1]), True, pygame.Color(0, 0, 0))                   
                    board_screen.blit(text, (CENTER_INDEX + (CENTER_INDEX / 2) + col * PIECE_SIZE, CENTER_INDEX * 2 + (CENTER_INDEX / 2) + row * PIECE_SIZE))

                # place the numbers in their respective column
                if col == 0:
                    font = pygame.font.SysFont(name = 'Calibri', size = 50)
                    text = font.render(str(CHESS_DIMENSION - row), True, pygame.Color(0, 0, 0))                   
                    board_screen.blit(text, (CENTER_INDEX - (CENTER_INDEX / 2) + col * PIECE_SIZE, CENTER_INDEX + (CENTER_INDEX / 2) + row * PIECE_SIZE))

    '''
    display the moveset box
    '''
    def display_moveset_box(self, board_screen):
        # create moves text
        font = pygame.font.SysFont(name = 'Calibri', size = 50)
        text = font.render("Moves", True, pygame.Color(0, 0, 0))

        # draw a black-bordered rectangle to put the move set inside
        x_cord = BOARD_DIMENSION  + CENTER_INDEX + CENTER_INDEX / 4
        y_cord = CENTER_INDEX
        width = BACKGROUND_WIDTH - CENTER_INDEX / 4 - x_cord 
        height = BOARD_DIMENSION

        board_screen.blit(text, (x_cord + width / (CENTER_INDEX / 4), y_cord - CENTER_INDEX / 2))

        pygame.draw.rect(board_screen, pygame.Color((0, 0, 0)), pygame.Rect(x_cord, y_cord, width, height), width = 1)


if __name__ == '__main__':
    ChessDisplay().main()