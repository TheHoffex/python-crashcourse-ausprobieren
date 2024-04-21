import pygame

class Player:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.size = 10
        self.speed = 10
        # self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        # pygame.draw.circle(self.screen, "red", self.player_pos, self.size)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill('RED')
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.player_pos.x += self.speed
