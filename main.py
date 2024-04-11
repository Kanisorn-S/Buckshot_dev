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
player1_full = pg.image.load('images/player1_full.png')
player1_red = pg.image.load('images/player1_red.png')
player1_eva = pg.image.load('images/player1_eva.png')
player2_full = pg.image.load("images/player2_full.png")
player2_red = pg.image.load("images/player2_red.png")
player2_eva = pg.image.load("images/player2_eva.png")
player_pics = [player1_full, player1_red, player1_eva, player2_full, player2_red, player2_eva]

# Initialize GameManager
gameManager = GameManager(window, player_pics, 10, gun, itemframe)

# Main program loop
while True:
    # check events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            # Let game manager handle the event
            gameManager.handleEvent(event)
    
    # Fill window's Background
    window.blit(background, (0, 0))
    
    # Frame update
    gameManager.update()
    gameManager.draw()
    pg.display.update()
    clock.tick(FRAMES_PER_SECOND)

    
    
    