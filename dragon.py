import pygame

class Dragon:
    "Class to manage dragon"
    
    def __init__(self, game):
        """Initialise dragon and location"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        
        # Load dragon image and resize
        self.img = pygame.image.load("images\dragon.png")
        self.img = pygame.transform.scale(self.img, (200, 100) )
        self.rect = self.img.get_rect()
        
        # Set dragon location to bottom middle
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store decimal value for dragon's horizontal position
        self.x = float(self.rect.x)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update dragon position according to movement flags"""
        # Update dragon's decimal x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right + 75:
            self.x += self.settings.dragon_speed
        if self.moving_left and self.rect.left > self.screen_rect.left - 75:
            self.x -= self.settings.dragon_speed
            
        # Update rect position from self.x    
        self.rect.x = self.x
    
    def draw_dragon(self):
        """Draw the dragon at its rect"""
        self.screen.blit(self.img, self.rect)        
        
    