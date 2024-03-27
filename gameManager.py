import pygame as pg
from pygame.locals import *
from gun import Gun 
from player import Player
from item import Item

class GameManager:
    def __init__(self, window, image, loc, nplayers, nbullets, gun):
        self.window = window
        self.image = image
        self.loc = loc
        self.rect = self.image.get_rect()
        self.locations = [(200, 400), (1080, 400)]
        self.nplayers = nplayers
        self.nbullets = nbullets
        self.playersInfo = self.loadPlayer()
        self.players = self.playersInfo.keys()
        self.gun = Gun(self.window, (640, 400), gun, nbullets, self.players)
        self.turn = 0

        
    def loadPlayer(self):
        Players = {}
        for i in range(self.nplayers):
            player = Player(self.window, 'images/heal.png', self.locations[i], i, f"Player{i}")
            Players[player] = player.health
        return Players
    
    def handleEvent(self, e):
        if e.key == pg.K_SPACE:
            self.gun.fire()
        elif e.key == pg.K_RIGHT:
            self.gun.aimRight()
        elif e.key == pg.K_LEFT:
            self.gun.aimLeft()

    def draw(self):
        self.window.blit(self.image, self.rect.topleft)
        for player in self.players:
            player.draw()
        self.gun.draw()