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
        # weights of [Heal, PotOfGreed, SuperCharger, GNDrive, DemonCore, AccessCard, Lasso]
        self.weights = [7/100, 7/100, 7/100, 7/100, 7/100, 7/100, 7/100]
        self.items = self.loadItem(nitems)


    def loadItem(self, nitems: int) -> deque:
        '''
        Load a random stack of items with nitems in it
        '''
        items = deque()
        for i in range(nitems):
            itemType = random.choices(range(7), self.weights, k = 1)[0]
            if itemType == 0:
                items.append(Heal(self.window))
            elif itemType == 1:
                items.append(PotOfGreed(self.window))
            elif itemType == 2:
                items.append(SuperCharger(self.window))
            elif itemType == 3:
                items.append(GNDrive(self.window))
            elif itemType == 4:
                items.append(DemonCore(self.window))
            elif itemType == 5:
                items.append(AccessCard(self.window))
            elif itemType == 6:
                items.append(Lasso(self.window))

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
