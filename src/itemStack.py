import pygame as pg
from pygame.locals import *
import random
from collections import deque
from src.item import *

class ItemStack():
    def __init__(self, window: pg.Surface, nitems: int):
        '''
        Initialize a stack of item to draw from
        '''
        self.window = window
        self.items = self.loadItem(nitems)


    def loadItem(self, nitems: int) -> deque:
        '''
        Load a random stack of items with nitems in it
        '''
        items = deque()
        for i in range(nitems):
            itemType = random.randint(0, 4) 
            if itemType == 0:
                items.append(Heal())
            elif itemType == 1:
                items.append(PotOfGreed())
            elif itemType == 2:
                items.append(SuperCharger())
            elif itemType == 3:
                items.append(GNDrive())
            elif itemType == 4:
                items.append(DemonCore())
            elif itemType == 5:
                items.append(AccessCard())
            elif itemType == 6:
                items.append(Lasso())

        return items
    
    def getItem(self) -> Item:
        '''
        Return the top most item on the stack
        '''
        # TODO
        return self.items.pop()

    def shuffle(self):
        '''
        Shuffle the item stack
        '''
        # TODO 
        random.shuffle(self.items)
        pass
