import pygame as pg
from pygame.locals import *
import random

class Bullet:
    # Class variable for the type of bullet
    BLANK = 0
    LIVE = 1
    LEFT = 0
    RIGHT = 1
    def __init__(self, window, odds):
        '''
        Initialize a single bullet
        Input : window - The main window of the game
                odds - A tuple of odds. The first is the probability of the bullet being a blank, 
                       the second is the probability of the bullet being a live
                image - A loaded image of the bullet flying
        Attributes : types - A list of types of bullet
                     type - The type of this bullet
                     damage - The damage of this bullet
        '''
        self.window = window
        self.fired_image = pg.transform.scale_by(pg.image.load('images/laser.png'), 0.01)
        self.rect = self.fired_image.get_rect(center=(300, 375/2))
        self.exact_pos = list(self.rect.topleft)
        self.types = [Bullet.BLANK, Bullet.LIVE]
        self.type = random.choices(self.types, odds)[0]
        self.damage = 1
        self.speed = 5
        self.aiming = Bullet.LEFT
        self.isFired = False
    
    def fired(self):
        '''
        Called when the bullet is fired from the gun.
        Set isFired to True to start drawing and updating the bullet
        Check for the direction the bullet needs to go
        '''
        # print('fired')
        self.isFired = True

    def update(self):
        '''
        Updates the bullet position 
        '''
    
        if self.isFired:
            # self.rect.x += self.speed
            self.exact_pos[0] += self.speed * (-1)**(self.aiming+1)
            self.rect.topleft = self.exact_pos
            # print(self.rect.x)

    def draw(self):
        '''
        Draws the bullet on the window if isFired is True
        '''
        if self.isFired:
            self.window.blit(self.fired_image, self.exact_pos)
        
        
        
        
    

    