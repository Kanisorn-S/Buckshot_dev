import pygame as pg
from pygame.locals import *
import pygwidgets as pw
import sys

pg.font.init()
font = pg.font.Font(size = 18)

class ScrollText:
    def __init__(self, window: pg.Surface, text: str, size: tuple[int, int], loc: tuple[int, int]):
        self.window = window
        self.w, self.h = size
        self.x, self.y = loc
        self.scroll = 0
        self.surface = pg.Surface((self.w + 30, self.h))
        self.surface.set_colorkey('black')
        # self.text = pw.DisplayText(self.surface, (0, 0), text, textColor='white', fontName='comicsans', fontSize=14)
        self.text = text
        self.tab_rect = pg.Rect(self.surface.get_width() - 20, 0, 20, self.surface.get_height())
        self.slider_rect = pg.Rect(self.surface.get_width() - 20, 0, 20, 40)

    def handleEvent(self, event: pg.event):
        pass
    
    def update(self):
        self.text_surface = font.render(self.text, False, 'white')

    def draw(self):
        pg.draw.rect(self.surface, "gray", self.tab_rect)
        pg.draw.rect(self.surface, "green", self.slider_rect)
        self.surface.blit(self.text_surface, (0, self.scroll))
        self.window.blit(self.surface, (self.x, self.y))

