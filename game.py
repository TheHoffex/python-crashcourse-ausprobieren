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
            self._check_events()
            self.wurm.update()                 
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.wurm.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.wurm.moving_left = True
        elif event.key == pygame.K_UP:
            self.wurm.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.wurm.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.wurm.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.wurm.moving_left = False
        elif event.key == pygame.K_UP:
            self.wurm.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.wurm.moving_down = False

if __name__ == '__main__':
    slither = Slither()
    slither.run_game()
