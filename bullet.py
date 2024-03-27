import pygame as pg
from pygame.locals import *
import random

class Bullet:
    # Class variable for the type of bullet
    BLANK = 0
    LIVE = 1
    def __init__(self, odds, image):
        '''
        Initialize a single bullet
        Input : odds - A tuple of odds. The first is the probability of the bullet being a blank, 
                       the second is the probability of the bullet being a live
                image - A loaded image of the bullet flying
        Attributes : types - A list of types of bullet
                     type - The type of this bullet
                     damage - The damage of this bullet
        '''
        self.image = image
        self.types = [Bullet.BLANK, Bullet.LIVE]
        self.type = random.choices(self.types, odds)
        self.damage = 1
    

    