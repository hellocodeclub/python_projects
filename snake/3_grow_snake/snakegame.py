import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

SNAKE_SQUARE_DIMENSIONS = 10

TOTAL_COLS = 60
TOTAL_ROWS = 40
surface_width = TOTAL_COLS * SNAKE_SQUARE_DIMENSIONS # 60 columns
surface_height = TOTAL_ROWS * SNAKE_SQUARE_DIMENSIONS # 40 rows
SNAKE_SPEED = 15

font_style = pygame.font.SysFont("bahnschrift", 10)

surface = pygame.display.set_mode((surface_width, surface_height))
pygame.display.set_caption('SNAKE GAME')

clock = pygame.time.Clock()

def draw_single_block(snake_block,color):
    vertical_position = snake_block[0] * SNAKE_SQUARE_DIMENSIONS
    horizontal_position = snake_block[1] * SNAKE_SQUARE_DIMENSIONS
    pygame.draw.rect(surface, color, [vertical_position, horizontal_position, SNAKE_SQUARE_DIMENSIONS, SNAKE_SQUARE_DIMENSIONS]) # origin position and dimensions

def draw_snake(snake_list):
    for snake_block in snake_list:
        draw_single_block(snake_block,green)

def move_block(col, row , direction):
    if direction == "LEFT":
        col = col -1
    if direction == "RIGHT":
        col = col +1
    if direction == "UP":
        row = row - 1
    if direction == "DOWN":
        row = row + 1

    return [col,row]

def detect_direction(direction, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            return "LEFT"
        elif event.key == pygame.K_RIGHT:
            return "RIGHT"
        elif event.key == pygame.K_UP:
            return "UP"
        elif event.key == pygame.K_DOWN:
            return "DOWN"
    return direction

def create_food_block():
    foodx = round(random.randrange(0, 59))
    foody = round(random.randrange(0, 39))
    return [foodx,foody]


def gameLoop():
    game_over = False

    # Snake Starting point
    x1 = 30
    y1 = 20

    direction = "UP"
    snake_list = [[30,21],[30,20]]

    food_block = create_food_block()

    snake_length = 2
    while not game_over:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            direction = detect_direction(direction, event)


        x1,y1 = move_block(x1,y1,direction)

        surface.fill(black)

        draw_single_block(food_block,red)

        snake_list.append([x1,y1])
        if(len(snake_list)>=snake_length):
            del snake_list[0]

        draw_snake(snake_list)

        pygame.display.update()

        if x1 == food_block[0] and y1 == food_block[1]:
            food_block = create_food_block()
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()


gameLoop()