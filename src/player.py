import pygame as pg
from src.bullet import Bullet
from pygame.locals import *



class Player:
    # Class Constants
    PWIDTH = 100
    PHEIGHT = 100
    HEART = pg.transform.scale_by(pg.image.load("images/heart.png"), 0.01)
    def __init__(self, window: pg.Surface, images: list, loc: tuple[int, int], id: int, name: str):
        '''
        Initialize a player.
        ------

        Input : window - The main playing window
                image - A tuple containing, in order, The image of the player and The image with green outline,
                        both already loaded by pg.image.load
                loc - The coordinates of the CENTER of the player image
                id - The id number use to identify a player. In a game with 2 players,
                      the first player has an index of 0 and the second player has an index of 1
                name - A string that represents the name of the player. Used to display on top as a name tag 
                      and at the end screen when the winner is announced
        
        Attribute : rect - pg.Rect that represents the player
                    health - Current health of the player
                    evading - Boolean, True when player used evading items, False by Default
                    canHeal - Boolean, False when player is on death-notice (health = 1), True by Default
        '''
        self.__window = window 
        self.image_full = pg.transform.scale_by(images[0], 0.05)
        self.image_red = pg.transform.scale_by(images[1], 0.05)
        self.image_eva = pg.transform.scale_by(images[2], 0.05)
        self.image = self.image_full
        w1 = pg.transform.rotate(self.image_full, 2)
        w2 = pg.transform.rotate(self.image_full, 1)
        w4 = pg.transform.rotate(self.image_full, -1)
        w5 = pg.transform.rotate(self.image_full, -2)
        self.wobble = [w1, w2, self.image_full, w4, w5]
        self.current_wobble = 2
        self.increasing = True
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.starting_y = loc[1]
        self.health = 3
        self.id = id
        self.name = name
        self.evading = False
        self.canHeal = True
        self.dy = 0
        self.floating_down = True

    def shot(self, bullet: Bullet):
        '''
        The function updates the players health according to the type of bullet being shot
        Input : bullet - An object of bullet class with the attributes type and damage
        If the type is "LIVE", the player's health is subtracted by the bullet's damage
        If the type is "BLANK", the player's health remains unchanged
        If the player has evasiveness, use it to determine whether the player takes damage from
        live rounds or not
        '''      
        if bullet.type == Bullet.LIVE:
            self.health -= bullet.damage
            bullet.aiming = self.id
            bullet.fired()

    def update(self):
        '''
        Update the player's image based on their current health and their evasive status
        '''
        if self.evading:
            self.image = self.image_eva
        elif self.health > 1:
            if self.increasing:
                self.current_wobble += 1
            else :
                self.current_wobble -= 1
            self.image = self.wobble[self.current_wobble]
            if (self.current_wobble == (len(self.wobble) - 1)) or (self.current_wobble == 0):
                self.increasing = not self.increasing
            if (self.dy >= 5) or (self.dy < 0):
                self.floating_down = not self.floating_down
            if self.floating_down:
                self.dy += 1
            else:
                self.dy -= 1
        elif self.health == 1:
            self.image = self.image_red
            self.canHeal = False
        
        

        

    def draw(self):
        '''
        Draws the player on the window using rect as position,
              the player's health bar on top of the player
        '''
        self.rect.center =  (self.rect.center[0], self.starting_y + self.dy)
        x, y = self.rect.topleft
        image = Player.HEART
        w, h = image.get_size()
        for i in range(self.health):
            rect = image.get_rect()
            rect.bottomleft = (x + (i * w), y)
            self.__window.blit(image, rect)
        self.__window.blit(self.image, self.rect)
