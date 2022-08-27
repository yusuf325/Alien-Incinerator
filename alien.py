import pygame
from pygame.sprite import Sprite

import random

class Alien(Sprite):
    """Class to manage aliens"""
    
    def __init__(self, game):
        "Intialise alien and location"
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        
        # Load and resize alien image
        self.image = pygame.image.load(r"images\alien.png")
        self.image = pygame.transform.scale(self.image, (50, 30))
        self.rect = self.image.get_rect()
        
        # Place alien at random location at top
        random_x = random.randint(self.rect.width/2, self.settings.screen_width - self.rect.width/2)
        self.rect.midbottom = (random_x, 0)
        
        # Store decimal value for alien's vertical position
        self.y = float(self.rect.y)
        
    def update(self):
        """Move alien down the screen"""
        # Update decimal position of alien
        self.y += self.settings.alien_speed
        
        # Update rect position from self.y
        self.rect.y = self.y
        
    def draw_alien(self):
        """Draw alien at its rect"""
        self.screen.blit(self.image, self.rect)