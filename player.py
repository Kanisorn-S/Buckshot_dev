import pygame as pg
from pygame.locals import *

PWIDTH = 100
PHEIGHT = 100

class Player:
    def __init__(self, window: pg.Surface, image: pg.Surface, loc: tuple[int, int], id: int, name: str):
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
        self.image = image
        self.rect = image.get_rect(center=loc)
        self.health = 100
        self.id = id
        self.name = name

    def shot(self, bullet):
        '''
        The function updates the players health according to the type of bullet being shot
        Input : bullet - An object of bullet class with the attributes type and damage
        If the type is "LIVE", the player's health is subtracted by the bullet's damage
        If the type is "BLANK", the player's health remains unchanged
        If the player has evasiveness, use it to determine whether the player takes damage from
        live rounds or not
        '''      
        # TODO
        pass

    def update(self):
        '''
        Update the player's health images to be displayed.
        Might implement more stuff later
        '''
        # TODO
        pass

    def draw(self):
        '''
        Draws the player on the window at loc,
              the player's name tag on top of the players head,
              the player's health bar at TBD.
              If it is the player's turn, draw the player_green pic instead of the normal pic
        '''
        # TODO
        self.__window.blit(self.image, self.rect)
