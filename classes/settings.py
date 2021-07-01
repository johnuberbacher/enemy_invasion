class Settings():
    # Class to keep settings
    def __init__(self):
        # Screen Settings
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1

        # Bullet Settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_limit = 3
