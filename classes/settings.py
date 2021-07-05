class Settings():
    # Class to keep settings
    def __init__(self):
        # Screen Settings
        self.screen_width = 1000
        self.screen_height = 640
        self.bg_color = (184, 179, 159)
        self.ship_speed_factor = 1

        # Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_limit = 55
