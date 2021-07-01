import sys
import pygame
from classes.bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # Respond to keydown events
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    # Respond to keyup events
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    # Update game screen with BG color
    screen.fill(ai_settings.bg_color)
    # Draw Bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Update game display and screen
    pygame.display.flip()

def fire_bullet(ai_settings, screen, ship, bullets):
    # Limit number of bullets allowed on screen at once
    if len(bullets) < ai_settings.bullets_limit:
        # Spawn Bullet and add to Group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
        bullets.update()
        # Remove bullets after passing outside the screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)