import pygame

TOTAL_COLS = 60
TOTAL_ROWS = 40
BLOCK_SIZE = 10

def draw_single_block(block_position, color):
    x = block_position[0] * BLOCK_SIZE
    y = block_position[1] * BLOCK_SIZE
    pygame.draw.rect(surface,color,(x,y,BLOCK_SIZE,BLOCK_SIZE))

def detect_direction(direction, event):
    if event.type== pygame.KEYDOWN:
        if event.key == pygame.K_LEFT :
            return "LEFT"
        elif event.key == pygame.K_RIGHT:
            return "RIGHT"
        elif event.key == pygame.K_UP:
            return "UP"
        elif event.key == pygame.K_DOWN:
            return "DOWN"
    return direction;

def move_block(column,row,direction):
    if direction == "LEFT":
        column = column - 1;
    if direction == "RIGHT":
        column = column + 1
    if direction == "UP":
        row = row -1
    if direction == "DOWN":
        row = row +1

    return [column,row]


pygame.init()
surface = pygame.display.set_mode((TOTAL_COLS*BLOCK_SIZE,
                                   TOTAL_ROWS*BLOCK_SIZE ))
pygame.display.set_caption('Snake game')
clock = pygame.time.Clock()

def gameLoop():
    game_over = False

    x1=30
    y1=20

    direction = "UP"
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            direction = detect_direction(direction, event)

        x1,y1 = move_block(x1,y1,direction)

        surface.fill((0,0,0))

        draw_single_block([x1,y1], (0,255,0)) #GREEN

        pygame.display.update()

        clock.tick(15)

gameLoop()
pygame.quit()




