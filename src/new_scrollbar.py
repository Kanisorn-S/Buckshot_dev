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
        self.text = text
        self.tab_rect = pg.Rect(self.surface.get_width() - 20, 0, 20, self.surface.get_height())
        self.slider_rect = pg.Rect(self.surface.get_width() - 20, 0, 20, 40)
        self.text_surface = font.render(self.text, False, 'white')
        self.speed = 5
        self.rect = self.surface.get_rect()

    def handleEvent(self, event: pg.event):
        if event.type == pg.MOUSEWHEEL:
            # event.y is 1 when scrolling up, -1 when scrolling down
            if not self.rect.collidepoint(pg.mouse.get_pos()):
                print(event.y)
                self.scroll = min(self.scroll + event.y * self.speed, 0)

    
    def update(self):

        self.slider_rect.top = max(-self.scroll, 0)

    def draw(self):
        self.surface.fill('black')
        pg.draw.rect(self.surface, "gray", self.tab_rect)
        pg.draw.rect(self.surface, "green", self.slider_rect)
        self.surface.blit(self.text_surface, (0, self.scroll))
        self.window.blit(self.surface, (self.x, self.y))

