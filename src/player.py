import pygame as pg
from src.bullet import Bullet
from pygame.locals import *

PWIDTH = 100
PHEIGHT = 100

class Player:
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
        
        Needed Attribute : isTurn - Boolean value. True when it is the player's turn, False when it is not
        '''
        self.__window = window 
        self.image_full = pg.transform.scale_by(images[0], 0.05)
        self.image_red = pg.transform.scale_by(images[1], 0.05)
        self.image_eva = pg.transform.scale_by(images[2], 0.05)
        self.image = self.image_eva
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.health = 3
        self.id = id
        self.name = name
        self.evading = False

    def shot(self, bullet: Bullet):
        '''
        The function updates the players health according to the type of bullet being shot
        Input : bullet - An object of bullet class with the attributes type and damage
        If the type is "LIVE", the player's health is subtracted by the bullet's damage
        If the type is "BLANK", the player's health remains unchanged
        If the player has evasiveness, use it to determine whether the player takes damage from
        live rounds or not
        '''      
        # TODO

        # print(bullet.type, Bullet.LIVE)
        if bullet.type == Bullet.LIVE:
            self.health -= bullet.damage
            bullet.aiming = self.id
            bullet.fired()
            print(f'ouch! {self.name} got hit! {self.health}/100')
        elif bullet.type == Bullet.BLANK:
            print('survived')

    def update(self):
        '''
        Update the player's health images to be displayed.
        Might implement more stuff later
        '''
        if self.health > 1:
            self.image = self.image_full
        elif self.health == 1:
            self.image = self.image_red
        if self.evading:
            self.image = self.image_eva

    def draw(self):
        '''
        Draws the player on the window at loc,
              the player's name tag on top of the players head,
              the player's health bar at TBD.
              If it is the player's turn, draw the player_green pic instead of the normal pic
        '''
        # TODO
        self.__window.blit(self.image, self.rect)
