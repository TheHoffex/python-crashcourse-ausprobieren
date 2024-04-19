import pygame

class Wurm:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.size = 10
        self.speed = 10
        player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        pygame.draw.circle(self.screen, "red", player_pos, self.size)

    def update(self):
        