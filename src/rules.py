import pygame as pg
from pygame.locals import *
import pygwidgets as pw
import sys
import random
from src.player import Player
from src.gameManager import GameManager

# Set const parameters
WIDTH = 600
HEIGHT = 375
FRAMES_PER_SECOND = 60
NPLAYER = 2


# Load necessary images
background = pg.image.load('images/background.jpg')

    

def rule_menu() -> int:
    clock = pg.time.Clock()
    window = pg.display.get_surface()
    backToMenuButton = pw.CustomButton(window, (300, 300), 'images/exit.png')
    backToMenuButton.setCenteredLoc((300, 335))
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif backToMenuButton.handleEvent(event):
                return 0
        
            

        window.blit(background, (0, 0))

        
        backToMenuButton.draw()

        
        pg.display.update()
        clock.tick(60)
        
            
    
        
    