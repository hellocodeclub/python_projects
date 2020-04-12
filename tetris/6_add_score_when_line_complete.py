import pygame, sys, time
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT,K_a,K_d
BLUE = (  0,   0, 155)
BOX_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOARD_WIDTH = 10
score = 0
# Added removeCompleteLines to remove complete lines and move everything above

def run_tetris_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('My Tetris')
    game_matrix = create_game_matrix()
    last_time_piece_moved = time.time()
    piece = create_piece()
    score=0
    while True:
        screen.fill((  0,   0,   0))
        if(time.time()-last_time_piece_moved > 0.1):
            piece['row'] = piece['row']+1
            last_time_piece_moved = time.time()

        draw_moving_piece(screen, piece)
        pygame.draw.rect(
            screen,
            BLUE,
            [100, 50, 10*20+10, 20*20+10], 5)

        draw_board(screen,game_matrix)
        draw_score(screen,score)

        listen_to_user_input(game_matrix, piece)

        if(piece['row']==19 or game_matrix[piece['row']+1][piece['column']]!='.'):
            game_matrix[piece['row']][piece['column']] = 'c'
            lines_removed = remove_completed_lines(game_matrix)
            score+=lines_removed
            piece = create_piece()

        pygame.display.update()
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

def draw_score(screen, score):
    # draw the score text
    # TO DO
    return

def remove_completed_lines(game_matrix):
    num_lines_removed = 0
    # TO DO
    return num_lines_removed

def is_line_completed(game_matrix, row):
     # TO DO
    return True

def listen_to_user_input(game_matrix,piece):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if (event.key == K_LEFT ) and isValidPosition(game_matrix,piece,adjColumn=-1):
                piece['column'] -= 1
            elif (event.key == K_RIGHT ) and isValidPosition(game_matrix,piece,adjColumn=1):
                piece['column'] += 1

def isOnBoard(row, column):
    return column >= 0 and column < 10 and row < 20

def isValidPosition(game_matrix, piece, adjColumn=0, adjRow=0):
    # Return True if the piece is within the board and not colliding
    if not isOnBoard(piece['row'] + adjRow, piece['column'] + adjColumn):
        return False
    if game_matrix[piece['row'] + adjRow][piece['column'] + adjColumn] != '.':
        return False
    return True

def create_piece():
    piece = {}
    piece['row'] = 0
    piece['column'] = 4
    return piece

def draw_board(screen,matrix):
    game_matrix_columns = 10
    game_matrix_rows = 20
    for row in range(game_matrix_rows):
        for column in range(game_matrix_columns):
            if(matrix[row][column]!='.'):
                draw_single_tetris_box(screen,row,column,(255,255,255), (217, 222, 226))

def draw_moving_piece(screen, piece):
    draw_single_tetris_box(screen,piece['row'],piece['column'],(255,255,255), (217, 222, 226))

def draw_single_tetris_box(screen, matrix_cell_row, matrix_cell_column,color,shadow_color):
    origin_x = 100 + 5 +(matrix_cell_column*20+1)
    origin_y = 50 + 5 + (matrix_cell_row*20+1)
    pygame.draw.rect(screen, shadow_color, [origin_x, origin_y, 20, 20])
    pygame.draw.rect(screen, color,[origin_x, origin_y,18,18])

def create_game_matrix():
    game_matrix_columns = 10
    game_matrix_rows = 20
    board = []
    for row in range(game_matrix_rows):
        new_row = []
        for column in range(game_matrix_columns):
            new_row.append('.')
        board.append(new_row)
    return board

run_tetris_game()