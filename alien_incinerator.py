import sys

import pygame

class AlienIncinerator:
    """Main class to manage game settings"""
    
    def __init__(self):
        """Initialise game attributes"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Incinerator")
    
    def run_game(self):
        """Start the game loop"""
        while True:
            # Wait for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update the screen
            pygame.display.flip()
            
if __name__ == "__main__":
    # Instantiate game and run
    game = AlienIncinerator()
    game.run_game()