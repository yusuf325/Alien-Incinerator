import sys

import pygame

from settings import Settings
from dragon import Dragon
from fireball import Fireball

class AlienIncinerator:
    """Main class to manage game"""
    
    def __init__(self):
        """Initialise game attributes"""
        pygame.init()
        
        self.settings = Settings()
        
        # Windowed mode
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        # Fullscreen mode 
        """self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height"""
        
        pygame.display.set_caption("Alien Incinerator")

        self.dragon = Dragon(self)
        self.fireballs = pygame.sprite.Group()
        
        self.bg_img = pygame.image.load(r"images\background.jpg")
        self.bg_img = pygame.transform.scale(self.bg_img,(self.settings.screen_width, self.settings.screen_height))
                
    def run_game(self):
        """Start the game loop"""
        while True:
            self._check_events()
            self.dragon.update()
            self.fireballs.update()
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
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._shoot_fireball()
            
    def _check_keyup(self, event):
        "Respond to key releases"
        if event.key == pygame.K_RIGHT:
            self.dragon.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.dragon.moving_left = False
    
    def _shoot_fireball(self):
        """Create new fireball and add to fireball group"""
        new_fireball = Fireball(self)
        self.fireballs.add(new_fireball)
        
    def _update_screen(self):
        """Update the screen"""
        self.screen.blit(self.bg_img, (0, 0))
        self.dragon.draw_dragon()
        for fireball in self.fireballs.sprites():
            fireball.draw_fireball()      
            
        pygame.display.flip()
                    
if __name__ == "__main__":
    # Instantiate game and run
    game = AlienIncinerator()
    game.run_game()