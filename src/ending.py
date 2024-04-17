import pygame as pg
from pygame.locals import *
import pygwidgets as pw
import sys
import random

# Set const parameters
WIDTH = 600
HEIGHT = 375
FRAMES_PER_SECOND = 60
NPLAYER = 2


# Load necessary images
background = pg.image.load('images/background.jpg')

    

def ending_menu() -> int:
    clock = pg.time.Clock()
    window = pg.display.get_surface()
    restartButton = pw.TextButton(window, (300, 300), 'RESTART')
    restartButton.setCenteredLoc((300, 200))
    backToMenuButton = pw.TextButton(window, (300, 300), 'BACK TO MENU')
    backToMenuButton.setCenteredLoc((300, 300))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if restartButton.handleEvent(event):
                return 1
            if backToMenuButton.handleEvent(event):
                return 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    pg.display.toggle_fullscreen()
        
        
        window.blit(background, (0, 0))

        backToMenuButton.draw()
        restartButton.draw()

        
        pg.display.update()
        clock.tick(60)
        
            
    
        
    