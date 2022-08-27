class Settings:
    """Class for all game settings"""
    
    def __init__(self):
        """Initialise settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # General settings
        self.fireball_rate = 200
        
        # Dragon settings
        self.dragon_speed = 3.5
        
        # Fireball settings
        self.fireball_speed = 1.5
        self.fireballs_allowed = 5
        
        # Alien settings
        self.alien_speed = 0.5