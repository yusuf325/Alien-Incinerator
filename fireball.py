import pygame
from pygame.sprite import Sprite

class Fireball(Sprite):
    """Class to manage fireballs from dragon"""
    
    def __init__(self, game):
        """Initialise fireball at dragon's position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        
        # Load fireball image and set position at dragon
        self.image = pygame.image.load(r"images\fireball.png")
        self.image = pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = game.dragon.rect.midtop
        
        # Allign position
        self.rect.x -= 3
        self.rect.y += 8
        
        # Store fireball's position as decimal value
        self.y = float(self.rect.y)
        
    def update(self):
        """Move fireball up the screen"""
        # Update decimal position of fireball
        self.y -= self.settings.fireball_speed
        
        # Update rect position from self.y
        self.rect.y = self.y
        
    def draw_fireball(self):
        "Draw the fireball at its rect"
        self.screen.blit(self.image, self.rect)