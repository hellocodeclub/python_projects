import pygame, sys
from pygame.locals import QUIT,KEYUP,K_ESCAPE

def run_tetris_game():
    pygame.init()  # start the game engine
    window_size = (640, 480)
    screen = pygame.display.set_mode(window_size) # create a window
    pygame.display.set_caption('My tetris') # give title to the window
    while True:
        screen.fill((  0,   0,   0))
        pygame.display.update()
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit() # terminate if any QUIT events are present

run_tetris_game()



