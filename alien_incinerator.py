import sys

import pygame

from settings import Settings
from dragon import Dragon

class AlienIncinerator:
    """Main class to manage game"""
    
    def __init__(self):
        """Initialise game attributes"""
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Incinerator")

        self.dragon = Dragon(self)
        
        self.bg_img = pygame.image.load(r"images\background.jpg")
        self.bg_img = pygame.transform.scale(self.bg_img,(self.settings.screen_width, self.settings.screen_height))
                
    def run_game(self):
        """Start the game loop"""
        i = 0

        while True:
            # Wait for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Update the screen
            self.screen.blit(self.bg_img, (0, 0))
            self.dragon.blitme()
            pygame.display.flip()
            
if __name__ == "__main__":
    # Instantiate game and run
    game = AlienIncinerator()
    game.run_game()