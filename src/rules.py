import pygame as pg
from pygame.locals import *
import pygwidgets as pw
import sys
import random
from src.player import Player
from src.gameManager import GameManager
from src.new_scrollbar import ScrollText
from src.raw_text import RAW_TEXT

# Set const parameters
WIDTH = 600
HEIGHT = 375
FRAMES_PER_SECOND = 60
NPLAYER = 2


# Load necessary images
background = pg.image.load('images/background.jpg')
raw_text = RAW_TEXT
rules = pg.transform.scale_by(pg.image.load('images/rules.png'), 1.2)
    

def rule_menu() -> int:
    clock = pg.time.Clock()
    window = pg.display.get_surface()
    backToMenuButton = pw.CustomButton(window, (300, 300), 'images/exit.png')
    backToMenuButton.setCenteredLoc((300, 335))
    scrollText = ScrollText(window, raw_text, (500, 200), (50, 100))
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if backToMenuButton.handleEvent(event):
                return 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    pg.display.toggle_fullscreen()
            scrollText.handleEvent(event)
            
        scrollText.update()

        window.blit(background, (0, 0))
        window.blit(rules, (250, 50))

        scrollText.draw()
        backToMenuButton.draw()
        
        pg.display.update()
        clock.tick(60)
        
            
    
        
    