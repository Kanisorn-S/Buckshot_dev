import pygame as pg
from pygame.locals import *
import pygwidgets as pw
import sys

class ScrollText:
    def __init__(self, window: pg.Surface, text: pw.DisplayText, hight: int):
        self.window = window
        self.text = text
        self.text_rect = text.getRect()
        self.loc = self.text_rect.topleft
        self.x, self.y = self.text_rect.topleft[0], self.text_rect.topleft[1]
        self.h = hight
        self.tab_rect = pg.Rect(self.x + self.text_rect.w + 10, self.y, 20, self.h)
        self.slider_rect = pg.Rect(self.x + self.text_rect.w + 10, self.y, 20, 40)

    def handleEvent(self, event: pg.event):
        pass
    
    def update(self):
        pass

    def draw(self):
        pg.draw.rect(self.window, "gray", self.tab_rect)
        pg.draw.rect(self.window, "green", self.slider_rect)
        self.text.draw()