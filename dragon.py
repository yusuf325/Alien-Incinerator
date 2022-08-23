import pygame

class Dragon:
    "Class to manage dragon"
    
    def __init__(self, game):
        """Initialise dragon"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        """Load dragon image"""
        self.img = pygame.image.load("images\dragon.png")
        self.img = pygame.transform.scale(self.img, (200, 100) )
        self.rect = self.img.get_rect()
        
        """Set dragon location to bottom middle"""
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw the dragon at its rect"""
        self.screen.blit(self.img, self.rect)        