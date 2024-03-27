import pygame as pg
from pygame.locals import *
import sys
from gameManager import GameManager
from item import Item
from player import Player
from gun import Gun 

WIDTH = 1280
HEIGHT = 800
FRAMES_PER_SECOND = 30

pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT), RESIZABLE|SCALED)
clock = pg.time.Clock()
bg = pg.image.load('images/background.png')
bg = pg.transform.scale(bg, (WIDTH, HEIGHT))
image1 = 'images/heal.png'
image2 = 'images/heal.png'
gun = 'images/evasiveness.png'

while True:
    gameManager = GameManager(window, bg, (0, 0), 2, 5, gun)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            gameManager.handleEvent(event)
            if event.key == pg.K_f:
                pg.display.toggle_fullscreen()
            if event.key == pg.K_k:
                gameManager.gun.update()
    window.fill('black')
    gameManager.draw()
    pg.display.update()
    clock.tick(FRAMES_PER_SECOND)
    