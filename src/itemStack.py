import pygame as pg
from pygame.locals import *
import random
from collections import deque
from item import Item 

class itemStack():
    def __init__(self, nitems: int):
        '''
        Initialize a stack of item to draw from
        '''
        self.items = self.loadItem(nitems)

    def loadItem(self, nitems: int) -> deque:
        '''
        Load a random stack of items with nitems in it
        '''
        items = deque()
        for i in range(nitems):
            itemType = random.randint(0, 10) 
            if itemType == 0:
                items.append(Heal())
            elif itemType == 1:
                items.append(PotOfGreed())
            elif itemType == 2:
                items.append(PowerAmp())
            elif itemType == 3:
                items.append(Reload())
            elif itemType == 4:
                items.append(Skip())
        return items
    
    def getItem(self) -> Item:
        '''
        Return the top most item on the stack
        '''
        # TODO
        pass

    def shuffle(self):
        '''
        Shuffle the item stack
        '''
        # TODO 
        pass
