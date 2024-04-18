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

    

def ending_menu(gameManager: GameManager) -> int:
    clock = pg.time.Clock()
    window = pg.display.get_surface()
    restartButton = pw.CustomButton(window, (300, 300), 'images/restart.png')
    restartButton.setCenteredLoc((300, 200))
    backToMenuButton = pw.CustomButton(window, (300, 300), 'images/exit.png')
    backToMenuButton.setCenteredLoc((300, 300))
    winner = gameManager.winner
    winner.rect.center = (300, 300)

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
        
        winner.update()
        
        window.blit(background, (0, 0))
        

        backToMenuButton.draw()
        restartButton.draw()
        winner.draw(False)

        
        pg.display.update()
        clock.tick(60)
        
            
    
        
    