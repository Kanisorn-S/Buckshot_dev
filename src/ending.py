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
gameover = pg.image.load('images/game_over.png')
gameover = pg.transform.scale_by(gameover, 0.5)
p1win = pg.image.load('images/p1_wins.png')
p1win = pg.transform.scale_by(p1win, 0.5)
p2win = pg.image.load('images/p2_wins.png')
p2win = pg.transform.scale_by(p2win, 0.5)

    

def ending_menu(gameManager: GameManager) -> int:
    clock = pg.time.Clock()
    window = pg.display.get_surface()
    restartButton = pw.CustomButton(window, (300, 300), 'images/restart.png')
    restartButton.setCenteredLoc((300, 290))
    backToMenuButton = pw.CustomButton(window, (300, 300), 'images/exit.png')
    backToMenuButton.setCenteredLoc((300, 335))
    winner = gameManager.winner
    image = None
    if winner.id == 0: # Player 1 wins
        image = p1win
    else:
        image = p2win
    image_rect = image.get_rect()
    gameover_rect = gameover.get_rect()
    image_rect.center = (300, 100)
    gameover_rect.center = (300, 50)

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
        
        winner.updateWin()
        
        window.blit(background, (0, 0))
        window.blit(gameover, gameover_rect)
        window.blit(image, image_rect)
        
        backToMenuButton.draw()
        restartButton.draw()
        winner.drawWin(window, (300, 190))

        
        pg.display.update()
        clock.tick(60)
        
            
    
        
    