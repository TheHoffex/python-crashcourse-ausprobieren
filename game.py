import pygame
import sys

from player import Player

class game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('MyGame')
        self.player = Player(self)

    def run_game(self):
        while True:
            self._check_events()
            self.player.update()                 
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
        if event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False

if __name__ == '__main__':
    game = game()
    game.run_game()
