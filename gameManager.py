import pygame as pg
from pygame.locals import *
from gun import Gun 
from player import Player
from item import Item

class GameManager:
    def __init__(self, window, nplayers, players_pic, nbullets, live_round, blank_round, gun):
        self.window = window
        self.nplayers = nplayers
        self.nbullets = nbullets
        self.players_pic = players_pic
        self.live_round = live_round
        self.blank_round = blank_round
        self.locations = [(100, 375/2), (500, 375/2)]
        self.playersInfo = self.loadPlayer()
        self.players = self.playersInfo.keys()
        self.gun = Gun(self.window, (640, 400), gun, nbullets, self.players)
        self.turn = 0
        self.winner = None

        
    def loadPlayer(self):
        Players = {}
        for i in range(self.nplayers):
            player = Player(self.window, self.players_pic[i], self.locations[i], i, f"Player{i}")
            Players[player] = player.health
        return Players
    
    def handleEvent(self, e):
        if e.key == pg.K_SPACE:
            target, bullet = self.gun.fire()
            target.shot(bullet)
            if target != self.players[self.turn]:
                self.turn = not self.turn
        elif e.key == pg.K_RIGHT:
            self.gun.aimRight()
        elif e.key == pg.K_LEFT:
            self.gun.aimLeft()
            
    def update(self):
        for player in self.players:
            player.update()
            self.playersInfo[player] = player.health
            if self.playersInfo[player] <= 0:
                del self.playersInfo[player]
        if not len(self.playersInfo.keys()):
            self.winner = self.playersInfo.keys()[0]
        self.gun.update()
        

    def draw(self):
        if self.winner is None:
            for player in self.players:
                player.draw()
            self.gun.draw()
        else:
            # show winning screen with victor at the center
            pass
