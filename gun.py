import pygame as pg
from pygame.locals import *
from collections import deque
from player import Player
from bullet import Bullet

class Gun:
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
        self.odds = [0.6, 0.4]
        self.bullets = self.load()
        self.players = players
        self.target = 69
        self.turning_left = False
        self.turning_right = False

    def load(self):
        bullets = deque()
        for _ in range(self.nbullets):
            bullets.append(Bullet(self.window, self.odds, self.image))
        return bullets
    
    def fire(self) -> tuple[Player, Bullet]:
        # print(f'fire {self.target}')
        return self.players[self.target], self.bullets.pop()
    
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