import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship and create rectangle from its image
        self.image = pygame.image.load('assets/img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set ship starting location
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom - 30
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        # self.rect.centerx = self.center

    def blitme(self):
        # Draw ship to given location
        self.screen.blit(self.image, self.rect)