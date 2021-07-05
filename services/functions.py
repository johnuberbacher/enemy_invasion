import sys
import pygame
from classes.bullet import Bullet
from classes.enemy import Enemy


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


def update_screen(ai_settings, screen, ship, bullets, enemies):
    # Update game screen with BG color
    screen.fill(ai_settings.bg_color)
    # Draw Bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    enemies.draw(screen)

    # Update game display and screen
    pygame.display.flip()


def fire_bullet(ai_settings, screen, ship, bullets):
    # Limit number of bullets allowed on screen at once
    if len(bullets) < ai_settings.bullets_limit:
        # Spawn Bullet and add to Group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, ship, bullets, enemies):
    bullets.update()
    # Remove bullets after passing outside the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_enemy_collisions(ai_settings, screen, ship, enemies, bullets)


def check_bullet_enemy_collisions(ai_settings, screen, ship, enemies, bullets):
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if len(enemies) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, enemies)


def get_number_enemies(ai_settings, enemy_width):
    available_space_x = ai_settings.screen_width - 2 * enemy_width
    number_enemies_x = int(available_space_x / (2 * enemy_width))
    return number_enemies_x


def get_number_rows(ai_settings, ship_height, enemy_height):
    available_space_y = (ai_settings.screen_height - (3 * enemy_height) - ship_height)
    number_rows = int(available_space_y / (2 * enemy_height))
    return number_rows


def create_enemy(ai_settings, screen, enemies, enemy_number, row_number):
    enemy = Enemy(ai_settings, screen)
    enemy_width = enemy.rect.width
    enemy.x = enemy_width + 2 * enemy_width * enemy_number
    enemy.rect.x = enemy.x
    enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
    enemies.add(enemy)


def create_fleet(ai_settings, screen, ship, enemies):
    enemy = Enemy(ai_settings, screen)
    number_enemies_x = get_number_enemies(ai_settings, enemy.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, enemy.rect.height)
    # play sound effect
    pygame.mixer.music.load('assets/ogg/fleet.ogg')
    pygame.mixer.music.play()
    for enemy_number in range(number_enemies_x):
        for row_number in range(number_rows):
            create_enemy(ai_settings, screen, enemies, enemy_number, row_number)
