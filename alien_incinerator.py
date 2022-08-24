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
        while True:
            self._check_events()
            self.dragon.update()
            self._update_screen()
            
    def _check_events(self):
        """Wait for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)  
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
                    
    def _check_keydown(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.dragon.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.dragon.moving_left = True
                      
    def _check_keyup(self, event):
        "Respond to key releases"
        if event.key == pygame.K_RIGHT:
            self.dragon.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.dragon.moving_left = False
            
    def _update_screen(self):
        """Update the screen"""
        self.screen.blit(self.bg_img, (0, 0))
        self.dragon.blit_me()
        
        pygame.display.flip()
                    
if __name__ == "__main__":
    # Instantiate game and run
    game = AlienIncinerator()
    game.run_game()