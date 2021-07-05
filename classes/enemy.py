import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, ai_settings, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('assets/img/enemy.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store Position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
