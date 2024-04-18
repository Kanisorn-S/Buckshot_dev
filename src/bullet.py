import pygame as pg
from pygame.locals import *
import random

class Bullet:
    # Class variable for the type of bullet
    BLANK = 0
    LIVE = 1
    LEFT = 0
    RIGHT = 1
    laser1 = pg.image.load('images/laser1.png')
    laser2 = pg.image.load('images/laser2.png')
    laser3 = pg.image.load('images/laser3.png')
    laser4 = pg.image.load('images/laser4.png')
    laser5 = pg.image.load('images/laser5.png')
    sprite = [laser1, laser2, laser3, laser3, laser3, laser3, laser3, laser3, laser4, laser5]
    sprite_right = [pg.transform.scale(image, (500, 100)) for image in sprite]
    sprite_left = [pg.transform.flip(image, 1, 0) for image in sprite_right]
    
    def __init__(self, window: pg.Surface, odds: tuple):
        '''
        Initialize a single bullet
        Input : window - The main window of the game
                odds - A tuple of odds. The first is the probability of the bullet being a blank, 
                       the second is the probability of the bullet being a live
        Attributes : fired_image - Load an image of a bullet while in flight
                     types - A list of types of bullet
                     type - The type of this bullet
                     damage - The damage of this bullet
                     speed - How fast a bullet is traveling in pixels/frame
                     aiming - The direction the bullet should move when it is fired
                     isFired - Boolean, If true then the bullet is fired
        '''
        self.window = window
        self.types = [Bullet.BLANK, Bullet.LIVE]
        self.type = random.choices(self.types, odds)[0]
        self.damage = 1
        self.speed = 5
        self.aiming = Bullet.LEFT
        self.isFired = False
        self.currentFrame = 0
        self.sprite = Bullet.sprite_left
        self.image = self.sprite[self.currentFrame]
        self.rect = self.image.get_rect()
        self.rect.midleft = (300, 270)
        self.timer = 0
    
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
        Updates the bullet position. Gamemanager only calls update on bullets that have been fired. 
        '''
        if self.isFired:
            if self.timer >= 4:
            # self.rect.x += self.speed
            # self.exact_pos[0] += self.speed * (-1)**(self.aiming+1)
            # self.rect.topleft = self.exact_pos
            # print(self.rect.x)
                if self.currentFrame < len(self.sprite) - 1:
                    self.currentFrame += 1
                else:
                    self.isFired = False
                self.timer = 0
            self.timer += 1
                
        if self.aiming == Bullet.RIGHT:
            self.sprite = Bullet.sprite_right
            self.image = self.sprite[self.currentFrame]
            self.rect = self.image.get_rect()
            self.rect.midleft = (270, 222)
        else:
             self.sprite = Bullet.sprite_left
             self.image = self.sprite[self.currentFrame]
             self.rect = self.image.get_rect()
             self.rect.midright = (350, 222)
        
            
            

    def draw(self):
        '''
        Draws the bullet on the window 
        '''
        if self.isFired:
            self.window.blit(self.sprite[self.currentFrame], self.rect)
        
        
        
        
    

    