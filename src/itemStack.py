import pygame as pg
from pygame.locals import *
import random
from collections import deque
from src.item import Item 

class ItemStack():
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
                pass 
                # items.append(Heal())
            elif itemType == 1:
                pass 
                # items.append(PotOfGreed())
            elif itemType == 2:
                pass
                # items.append(PowerAmp())
            elif itemType == 3:
                pass
                # items.append(Reload())
            elif itemType == 4:
                pass
                # items.append(Skip())
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
