import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):  #ai_game is passed to be able to be initiated 
        """Initialize the ship and set its starting position.""" #inside the main game 
        self.screen = ai_game.screen                             #initiation and also use the attributes that come ith the main initiation.
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.moving_right = False
        self.moving_left = False

        # Load the ship image and get its rect.
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)