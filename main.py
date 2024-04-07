# Import Libs
import pygame as pg
from pygame.locals import *
import sys
from src.gameManager import GameManager
from src.item import Item
from src.player import Player
from src.gun import Gun


# Set const parameters
WIDTH = 600
HEIGHT = 375
FRAMES_PER_SECOND = 60
NPLAYER = 2
NBULLETS = 5

# Initialize pygame
pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT), RESIZABLE | SCALED)
clock = pg.time.Clock()

# Load necessary images
background = pg.image.load('images/background.jpg')
gun = pg.image.load('images/evasiveness.png')
heal = pg.image.load('images/heal.png')
heal = pg.transform.scale_by(heal, 0.05)
pot_of_greed = pg.image.load('images/pot_of_greed.png')
power_amp = pg.image.load('images/power_amp.png')
skip = pg.image.load('images/skip.png')
itemframe = pg.image.load('images/itembox.png')
heart = pg.image.load('images/heart.png')


gameManager = GameManager(window, 2, 2*[heal], 10, gun, itemframe, heart)
# Main program loop
while True:
    # Initialize game manager
    # gameManager = GameManager(window, background, (0, 0), NPLAYER, NBULLETS, evasiveness, gun)
    
    # check events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            # Let game manager handle the event
            gameManager.handleEvent(event)
    
    window.blit(background, (0, 0))
    gameManager.update()
    gameManager.draw()
    pg.display.update()
    clock.tick(FRAMES_PER_SECOND)

    
    
    