import pygame
import sys

from wurm import Wurm

class Slither:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('MyGame')
        self.wurm = Wurm(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    

            pygame.display.flip()

if __name__ == '__main__':
    slither = Slither()
    slither.run_game()
