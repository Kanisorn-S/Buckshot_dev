import pygame as pg
from pygame.locals import *
from collections import deque
from player import Player
from bullet import Bullet

class Gun:
    BLANK_IMG = pg.transform.scale_by(pg.image.load('images/blank_shot.png'), 0.02)
    LIVE_IMG = pg.transform.scale_by(pg.image.load('images/live_shot.png'), 0.02)
    IMG_W = LIVE_IMG.get_size()[0]
    def __init__(self, window, loc, nbullets, players):
        self.window = window
        self.nbullets = nbullets
        self.sprites = []
        for i in range(1, 6):
            image = pg.image.load(f'images/gun_{i}.png')
            self.sprites.append(pg.transform.scale_by(image, 0.08))
        self.current_sprite = 2
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.odds = [0.5, 0.5]
        self.bullets = self.load()
        self.players = players
        self.target = 69
        self.turning_left = False
        self.turning_right = False
        self.live = 0
        self.blank = 0
        for bullet in self.bullets:
            if bullet.type == Bullet.LIVE:
                self.live += 1
            else:
                self.blank += 1

    def load(self):
        bullets = deque()
        for _ in range(self.nbullets):
            bullets.append(Bullet(self.window, self.odds, self.image))
        return bullets
    
    def fire(self) -> tuple[Player, Bullet]:
        # print(f'fire {self.target}')
        bullet = self.bullets.pop()
        if bullet.type == Bullet.LIVE:
            self.live -= 1
        else:
            self.blank -= 1
        return self.players[self.target], bullet
    
    def aimRight(self):
        if self.target == 1:
            return
        self.turning_right = True
        self.target = 1
    
    def aimLeft(self):
        if self.target == 0:
            return
        self.turning_left = True
        self.target = 0
            
    def update(self):
        # print("Current bullets: ", [bullet.type for bullet in self.bullets])
        # print(self.target)
        if len(self.bullets) == 0:
            self.bullets = self.load()
        if self.turning_left:
            print(self.current_sprite)
            self.current_sprite += 1
            if self.current_sprite >= (len(self.sprites) - 1):
                self.turning_left = False
            self.image = self.sprites[self.current_sprite]
        elif self.turning_right:
            self.current_sprite -= 1
            if self.current_sprite <= 0:
                self.turning_right = False
            self.image = self.sprites[self.current_sprite]

                  

    def draw(self):
        self.window.blit(self.image, self.rect)
        x = 300
        y = 330
        for i in range(self.live):
            rect = Gun.LIVE_IMG.get_rect()
            rect.topright = (x - (i * Gun.IMG_W), y)
            self.window.blit(Gun.LIVE_IMG, rect)
        for i in range(self.blank):
            rect = Gun.BLANK_IMG.get_rect()
            rect.topleft = (x + (i * Gun.IMG_W), y)
            self.window.blit(Gun.BLANK_IMG, rect)