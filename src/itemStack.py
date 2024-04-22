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
        self.weights = [0.16, 0.04, 0.16, 0.16, 0.16, 0.16, 0.16]
        self.items = self.loadItem(nitems)


    def loadItem(self, nitems: int) -> deque:
        '''
        Load a random stack of items with nitems in it
        '''
        items = deque()
        for i in range(nitems):
            itemType = random.choices(range(7), self.weights, k = 1)[0]
            match itemType:
                case 0:
                    items.append(Heal(self.window))
                case 1:
                    items.append(PotOfGreed(self.window))
                case 2:
                    items.append(SuperCharger(self.window))
                case 3:
                    items.append(GNDrive(self.window))
                case 4:
                    items.append(DemonCore(self.window))
                case 5:
                    items.append(AccessCard(self.window))
                case 6:
                    items.append(Lasso(self.window))

        return items
    
    def getItem(self) -> Item:
        '''
        Return the top most item on the stack
        '''
        return self.items.pop()

    def shuffle(self):
        '''
        Shuffle the item stack
        '''
        random.shuffle(self.items)
