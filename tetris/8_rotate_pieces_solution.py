import pygame, sys, time, random
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT,K_UP,K_DOWN,K_a,K_d
BLUE = (  0,   0, 155)
BOX_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOARD_WIDTH = 10
score = 0

S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..cc.',
                     '.cc..',
                     '.....'],
                    ['.....',
                     '..c..',
                     '..cc.',
                     '...c.',
                     '.....']]

I_SHAPE_TEMPLATE = [['..c..',
                     '..c..',
                     '..c..',
                     '..c..',
                     '.....'],
                    ['.....',
                     '.....',
                     'cccc.',
                     '.....',
                     '.....']]
O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.cc..',
                     '.cc..',
                     '.....']]
def available_tetris_pieces():
    return {
        'S':S_SHAPE_TEMPLATE,
        'I':I_SHAPE_TEMPLATE,
        'O':O_SHAPE_TEMPLATE
    }

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
        if(time.time()-last_time_piece_moved > 0.3):
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
        if(not isValidPosition(game_matrix,piece,adjRow=1)):
            game_matrix = update_game_matrix(game_matrix,piece)
            lines_removed = remove_completed_lines(game_matrix)
            score+=lines_removed
            piece = create_piece()

        pygame.display.update()
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

def create_piece():
    piece = {}
    random_shape = random.choice(list(available_tetris_pieces().keys()))
    piece['shape'] = random_shape
    piece['rotation'] = 0
    piece['column'] = 2  # update from 4
    piece['row'] = 0
    return piece

def draw_moving_piece(screen, piece):
    shape_to_draw = available_tetris_pieces()[piece['shape']][piece['rotation']]
    for row in range(5):
        for col in range(5):
            if shape_to_draw[row][col] !='.':
                draw_single_tetris_box(screen,piece['row']+row,piece['column']+col,(255,255,255), (217, 222, 226))

def update_game_matrix(matrix, piece):
    for row in range(5):
        for col in range(5):
            if(available_tetris_pieces()[piece['shape']][piece['rotation']][row][col] != '.'):
                matrix[piece['row']+row][piece['column']+col] = 'c'
    return matrix

def isValidPosition(game_matrix, piece, adjColumn=0, adjRow=0):
    # Return True if the every block of the piece is within the board and not colliding
    piece_matrix = available_tetris_pieces()[piece['shape']][piece['rotation']]
    for row in range(5):
        for col in range(5):
            if piece_matrix[row][col] == '.':
                continue
            if not isOnBoard(piece['row']+ row + adjRow, piece['column']+ col + adjColumn):
                return False
            if game_matrix[piece['row']+ row + adjRow][piece['column'] +col + adjColumn] != '.':
                return False

    return True

def draw_score(screen, score):
    # draw the score text
    font = pygame.font.Font('freesansbold.ttf', 18)
    scoreSurf = font.render('Score: %s' % score, True, (255,255,255))
    screen.blit(scoreSurf, (640 - 150, 20))

def remove_completed_lines(game_matrix):
    num_lines_removed = 0
    for row in range(20):
        if(is_line_completed(game_matrix,row)):
            for row_to_move_down in range(row, 0, -1):
                for column in range(10):
                    game_matrix[row_to_move_down][column] = game_matrix[row_to_move_down-1][column]
            # Set very top line to blank.
            for x in range(10):
                game_matrix[0][x] = '.'
            num_lines_removed += 1
    return num_lines_removed


def is_line_completed(game_matrix, row):
    # Return True if the line filled with boxes with no gaps.
    for column in range(10):
        if game_matrix[row][column] == '.':
            return False
    return True

def listen_to_user_input(game_matrix,piece):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if (event.key == K_LEFT ) and isValidPosition(game_matrix,piece,adjColumn=-1):
                piece['column'] -= 1
            elif (event.key == K_RIGHT ) and isValidPosition(game_matrix,piece,adjColumn=1):
                piece['column'] += 1
            elif (event.key == K_UP):
                piece['rotation'] = (piece['rotation']+1) % len(available_tetris_pieces()[piece['shape']])
                if not isValidPosition(game_matrix, piece):
                    piece['rotation'] = (piece['rotation']-1) % len(available_tetris_pieces()[piece['shape']])

def isOnBoard(row, column):
    return column >= 0 and column < 10 and row < 20

def draw_board(screen,matrix):
    game_matrix_columns = 10
    game_matrix_rows = 20
    for row in range(game_matrix_rows):
        for column in range(game_matrix_columns):
            if(matrix[row][column]!='.'):
                draw_single_tetris_box(screen,row,column,(255,255,255), (217, 222, 226))

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