import pygame as pg
from src.bullet import Bullet
from pygame.locals import *
import math



class Player:
    # Class Constants
    PWIDTH = 100
    PHEIGHT = 100
    HEART = pg.transform.scale_by(pg.image.load("images/heart.png"), 0.03)
    BROKEN = pg.transform.scale(pg.image.load('images/broken_heart.png'), HEART.get_size())
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
        '''
        # Normal initialization
        self.__window = window 
        self.image_full = pg.transform.scale_by(images[0], 0.05)
        self.image_red = pg.transform.scale_by(images[1], 0.05)
        self.image_eva = pg.transform.scale_by(images[2], 0.05)
        self.image = self.image_full
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.health = 5
        self.death_notice = math.ceil(self.health / 3)
        self.id = id
        self.name = name
        self.evading = False
        self.canHeal = True
        
        # Wobble full effect
        w1 = pg.transform.rotate(self.image_full, 4)
        w2 = pg.transform.rotate(self.image_full, 3)
        w3 = pg.transform.rotate(self.image_full, 2)
        w4 = pg.transform.rotate(self.image_full, 1)
        w6 = pg.transform.rotate(self.image_full, -1)
        w7 = pg.transform.rotate(self.image_full, -2)
        w8 = pg.transform.rotate(self.image_full, -3)
        w9 = pg.transform.rotate(self.image_full, -4)
        self.wobble = [w1, w2, w3, w4, self.image_full, w6, w7, w8, w9]
        self.current_wobble = 2
        self.increasing = True

        # Wobble red effect
        wr1 = pg.transform.rotate(self.image_red, 4)
        wr2 = pg.transform.rotate(self.image_red , 3)
        wr3 = pg.transform.rotate(self.image_red, 2)
        wr4 = pg.transform.rotate(self.image_red, 1)
        wr6 = pg.transform.rotate(self.image_red, -1)
        wr7 = pg.transform.rotate(self.image_red, -2)
        wr8 = pg.transform.rotate(self.image_red, -3)
        wr9 = pg.transform.rotate(self.image_red, -4)
        self.wobble_red = [wr1, wr2, wr3, wr4, self.image_red, wr6, wr7, wr8, wr9]

        # Wobble evade effect
        we1 = pg.transform.rotate(self.image_eva, 4)
        we2 = pg.transform.rotate(self.image_eva, 3)
        we3 = pg.transform.rotate(self.image_eva, 2)
        we4 = pg.transform.rotate(self.image_eva, 1)
        we6 = pg.transform.rotate(self.image_eva, -1)
        we7 = pg.transform.rotate(self.image_eva, -2)
        we8 = pg.transform.rotate(self.image_eva, -3)
        we9 = pg.transform.rotate(self.image_eva, -4)
        self.wobble_eva = [we1, we2, we3, we4, self.image_eva, we6, we7, we8, we9]
        
        # Floating effect
        self.starting_y = loc[1]
        self.dy = 0
        self.floating_down = True
        
        # Delay frame update
        self.timer = 0
        self.frame = 2

        # Items
        self.items = []

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
        self.timer += 1
        if self.evading:
            self.image = self.image_eva
            self.wobble = self.wobble_eva
        elif self.health <= self.death_notice:
            self.image = self.image_red
            self.wobble = self.wobble_red
            self.canHeal = False
            self.frame = 1
        if self.timer >= self.frame:
            self.timer = 0
            if self.increasing:
                self.current_wobble += 1
            else :
                self.current_wobble -= 1
            self.image = self.wobble[self.current_wobble]
            if (self.current_wobble == (len(self.wobble) - 1)) or (self.current_wobble == 0):
                self.increasing = not self.increasing
            if (self.dy >= 10) or (self.dy < 0):
                self.floating_down = not self.floating_down
            if self.floating_down:
                self.dy += 1
            else:
                self.dy -= 1
        
        

        

    def draw(self, displayHealth = True):
        '''
        Draws the player on the window using rect as position,
              the player's health bar on top of the player
        '''
        self.rect.center =  (self.rect.center[0], self.starting_y + self.dy)
        if displayHealth:
            x, y = self.rect.topleft
            image = Player.HEART
            broken = Player.BROKEN
            w, h = image.get_size()
            for i in range(self.health):
                rect = image.get_rect()
                rect.bottomleft = (x + (i * w), y)
                if i < self.death_notice:
                    self.__window.blit(broken, rect)
                else:
                    self.__window.blit(image, rect)
        else:
            self.image = pg.transform.scale_by(self.image, 3)
            self.rect = self.image.get_rect()
        self.__window.blit(self.image, self.rect)
