import random
import pygame
import time
import sys
from pygame.locals import QUIT

class DrawDemo:

    def create_game_window(self):
        init_result = pygame.init()
        if init_result[1] !=0:
            print('pygame not installed')
            return

        width = 800
        height = 600
        size = (width, height)
        self.surface = pygame.display.set_mode(size)
        pygame.display.set_caption('Drawing example')

    def draw_random_art(self):

        white = (255,255,255)

        while(True):
            self.surface.fill(white)

            for count in range(100):
                start = DrawDemo.get_random_coordinate()
                end = DrawDemo.get_random_coordinate()
                color = DrawDemo.get_random_color()
                pygame.draw.line(self.surface, color, start, end)

            for count in range(100):
                pos = DrawDemo.get_random_coordinate()
                color = DrawDemo.get_random_color()
                radius = random.randint(5,50)
                pygame.draw.circle(self.surface, color, pos, radius)

            pygame.display.flip()
            pygame.time.delay(1000)
            if event in pygame.event.get(QUIT):
                pygame.quit()
                sys.exit()

    @staticmethod
    def get_random_coordinate():
        width = 800
        height = 600
        X = random.randint(0,width-1)
        Y = random.randint(0, height-1)
        return (X,Y)

    @staticmethod
    def get_random_color():
        red = random.randint(0, 255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        return (red,green,blue)



game = DrawDemo()
game.create_game_window()

game.draw_random_art()



