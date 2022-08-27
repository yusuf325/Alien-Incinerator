class GameStats:
    """Class to manage game statistics"""
    
    def __init__(self, game):
        """Initialise statistics"""
        self.settings = game.settings
        self.game_active = True
        self.dragons_left = self.settings.dragon_limit
        