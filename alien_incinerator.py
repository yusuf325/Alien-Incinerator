import sys

import pygame

from settings import Settings
from game_stats import GameStats
from dragon import Dragon
from fireball import Fireball
from alien import Alien

class AlienIncinerator:
    """Main class to manage game"""
    
    def __init__(self):
        """Initialise game attributes"""
        pygame.init()
        
        self.settings = Settings()
        self.stats = GameStats(self)
        
        # Windowed mode
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        
        # Fullscreen mode 
        """self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height"""
        
        pygame.display.set_caption("Alien Incinerator")

        # Instantiate game entities
        self.dragon = Dragon(self)
        self.fireballs = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        # Load and resize background iamge
        self.bg_img = pygame.image.load(r"images\background.jpg")
        self.bg_img = pygame.transform.scale(self.bg_img,(self.settings.screen_width, self.settings.screen_height))
                
    def run_game(self):
        """Start the game loop"""
        i = 0
        while True:
            self._check_events()
            if self.stats.game_active:
                self.dragon.update()
                self._update_fireballs()
                self._update_aliens(i)
            self._update_screen()
            i += 1 
            
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
        """Create new fireball and add to fireballs group"""
        if len(self.fireballs) < self.settings.fireballs_allowed:
            new_fireball = Fireball(self)
            self.fireballs.add(new_fireball)
    
    def _update_fireballs(self):
        """Update position of fireballs and delete old fireballs"""
        # Update fireball positions
        self.fireballs.update()
        
        # Delete fireballs that have gone off screen
        for fireball in self.fireballs.copy():
            if fireball.rect.bottom <= 0:
                self.fireballs.remove(fireball)
                
        # Check for bullets that have hit an alien and remove both
        collisions = pygame.sprite.groupcollide(self.fireballs, self.aliens, True, True)       
         
    def _update_aliens(self, i):
        """Release alien and update alien positions"""
        # Release a new alien at a certain rate
        if i % self.settings.alien_rate == 0:
            self._release_alien()
        self.aliens.update()
        
        # Remove aliens that have gone off screen
        for alien in self.aliens.copy():
            if alien.rect.top >= self.settings.screen_height:
                self.stats.dragons_left -= 1
                if self.stats.dragons_left == 0:
                    self.stats.game_active = False
                self.aliens.remove(alien)
                
        # Removes all aliens and restarts ship
        """if pygame.sprite.spritecollideany(self.dragon, self.aliens):
            self.aliens.empty()
            self.dragon = Dragon(self)
            print("Ship hit!!!")"""
        # Just removes the alien
        """collider = pygame.sprite.spritecollideany(self.dragon, self.aliens)
        if collider:
            self.aliens.remove(collider)
            print("Ship hit")"""
        
    def _release_alien(self):
        """Create new alien and add to aliens group"""
        new_alien = Alien(self)
        self.aliens.add(new_alien)
        
    def _update_screen(self):
        """Update the screen"""
        self.screen.blit(self.bg_img, (0, 0))
        self.dragon.draw_dragon()
        #for fireball in self.fireballs.sprites():
           # fireball.draw_fireball()      
        self.fireballs.draw(self.screen)
        #for alien in self.aliens.sprites():
            #alien.draw_alien()
        self.aliens.draw(self.screen)        
         
        pygame.display.flip()
                    
if __name__ == "__main__":
    # Instantiate game and run
    game = AlienIncinerator()
    game.run_game()