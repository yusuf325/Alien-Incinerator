class GameStats:
    """Class to manage game statistics"""
    
    def __init__(self, game):
        """Initialise statistics"""
        self.settings = game.settings
        self.reset_stats()
        
        # Start game in an active state
        self.game_active = False

    def reset_stats(self):
        """Initialise stats that can change during the game"""
        self.dragons_left = self.settings.dragon_limit
        