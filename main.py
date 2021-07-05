import pygame
from pygame.sprite import Group
from classes.settings import Settings
from classes.ship import Ship
from services import functions as game_functions


def run_game():
    # Initialize game loop and create screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    # Program Name
    pygame.display.set_caption("Enemy Invasion")

    # Create player ship
    ship = Ship(ai_settings, screen)
    # Create Group to store live bullets
    # Create Group outside of Game Loop to avoid never-ending loops, crashes or freezes
    bullets = Group()
    enemies = Group()

    # Spawn Enemies
    game_functions.create_fleet(ai_settings, screen, ship,  enemies)

    # Start game loop
    while True:
        game_functions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(ai_settings, screen, ship, bullets, enemies)
        game_functions.update_screen(ai_settings, screen, ship, bullets, enemies)


run_game()

