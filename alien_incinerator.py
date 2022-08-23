import sys

import pygame

class AlienIncinerator:
    """Main class to manage game settings"""
    
    def __init__(self):
        """Initialise game attributes"""
        pygame.init()
        
        self.width, self.height = 1200, 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Alien Incinerator")

        #self.bg_colour = (82, 139, 167)
        self.bg_img = pygame.image.load(r"images\background.jpg")
        self.bg_img = pygame.transform.scale(self.bg_img,(self.width, self.height))
                
    def run_game(self):
        """Start the game loop"""
        i = 0

        while True:
            # Wait for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Update the screen
             #self.screen.fill(self.bg_colour)
            self.screen.blit(self.bg_img, (0, 0))
            pygame.display.flip()
            
if __name__ == "__main__":
    # Instantiate game and run
    game = AlienIncinerator()
    game.run_game()