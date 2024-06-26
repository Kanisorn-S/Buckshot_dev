import pygame as pg
from pygame.locals import *
import pygwidgets as pw
import sys

pot_of_greed = pg.image.load('images/rule_pic/pot_of_greed_r.png')
power_amp = pg.image.load('images/rule_pic/power_amp_r.png')
gn_drive = pg.image.load('images/rule_pic/evasiveness_r.png')
skip = pg.image.load('images/rule_pic/skip_r.png')
heal = pg.image.load('images/rule_pic/heal_r.png')
access_card = pg.image.load('images/rule_pic/reload_r.png')
lasso = pg.image.load('images/rule_pic/lasso_r.png')
rule_pics = [pot_of_greed, power_amp, gn_drive, skip, heal, access_card, lasso]
rule_pics = [pg.transform.scale(pic, (52, 52)) for pic in rule_pics]


class ScrollText:
    def __init__(self, window: pg.Surface, text: str, size: tuple[int, int], loc: tuple[int, int]):
        self.window = window
        self.w, self.h = size
        self.x, self.y = loc
        self.scroll = 0
        self.bar_scroll = 0
        self.surface = pg.Surface((self.w + 30, self.h))
        self.surface.set_colorkey('black')
        self.text = text
        self.text_surface = pw.DisplayText(self.surface, (0, self.scroll), text, textColor='white')
        self.tab_rect = pg.Rect(self.surface.get_width() - 20, 0, 20, self.surface.get_height())
        self.slider_rect = pg.Rect(self.surface.get_width() - 20, 0, 20, 40)
        self.item_surface = pw.DisplayText(self.surface, (0, self.scroll + 190), "Items", fontSize=28, textColor='white')
        self.speed = 5
        self.rect = pg.Rect(self.x, self.y, self.w + 30, self.h)

    def handleEvent(self, event: pg.event):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if event.type == pg.MOUSEWHEEL:
            # event.y is 1 when scrolling up, -1 when scrolling down

                self.scroll = max(-580, min(self.scroll + event.y * self.speed, 0))
                self.bar_scroll = -self.scroll * (self.h - 40) / 580

    
    def update(self):
        self.text_surface.setLoc((0, self.scroll))
        self.item_surface.setLoc((0, self.scroll + 190))
        self.slider_rect.top = min(max(self.bar_scroll, 0), self.h - 40)

    def draw(self):
        self.surface.fill('black')
        pg.draw.rect(self.surface, "lightgray", self.tab_rect, border_radius=3)
        pg.draw.rect(self.surface, "darkgray", self.slider_rect, border_radius=3)
        self.item_surface.draw()
        self.text_surface.draw()
        for i, pic in enumerate(rule_pics):
            self.surface.blit(pic, (50, self.scroll + 300 + (i * 70)))
        self.window.blit(self.surface, (self.x, self.y))

