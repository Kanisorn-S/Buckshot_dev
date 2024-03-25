import pygame as pg
from pygame.locals import *

PWIDTH = 100
PHEIGHT = 100

class Player:
    def __init__(self, window, image, loc, id, name):
        self.window = window
        self.image = self.scale(image)
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.id = id
        self.name = name
        self.items = []
        self.health = 3
        self.evasiveness = 0
        
    def scale(self, image):
        scaled = pg.image.load(image)
        scaled = pg.transform.scale(scaled, (PWIDTH, PHEIGHT))
        return scaled
        
    def update():
        pass

    def draw(self):
        self.window.blit(self.image, self.rect.topleft)
        