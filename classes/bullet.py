import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        # Spawn bullet from ships current position when fired
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position
        self.image = pygame.image.load('assets/img/bullet.bmp')
        self.rect = self.image.get_rect()

        #self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store position of bullet as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        # play sound effect
        pygame.mixer.music.load('assets/ogg/bullet.ogg')
        pygame.mixer.music.play()

    def update(self):
        # Move Bullet
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)

