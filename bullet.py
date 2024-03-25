import pygame as pg
from pygame.locals import *
import random

class Bullet:
    def __init__(self, odds):
        self.types = [0, 1]
        self.type = random.choices(self.types, odds)
    