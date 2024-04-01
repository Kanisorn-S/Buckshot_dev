import pygame as pg
from pygame.locals import *
from collections import deque
from player import Player
from bullet import Bullet

class Gun:
    def __init__(self, window, loc, image, nbullets, players):
        self.window = window
        self.nbullets = nbullets
        self.image = image
        self.image = pg.transform.scale(self.image, (100, 100))
        self.image_flipped = pg.transform.flip(self.image, 1, 0)
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.odds = [0.6, 0.4]
        self.bullets = self.load()
        self.players = players
        self.target = 0

    def load(self):
        bullets = deque()
        for _ in range(self.nbullets):
            bullets.append(Bullet(self.window, self.odds, self.image))
        return bullets
    
    def fire(self) -> tuple[Player, Bullet]:
        # print(f'fire {self.target}')
        return self.players[self.target], self.bullets.pop()
    
    def aimRight(self):
        self.target = 1
    
    def aimLeft(self):
        self.target = 0
            
    def update(self):
        # print("Current bullets: ", [bullet.type for bullet in self.bullets])
        # print(self.target)
        if len(self.bullets) == 0:
            self.bullets = self.load()
        pass

            

    def draw(self):
        if self.target:
            self.window.blit(self.image_flipped, self.rect)
        else:
            self.window.blit(self.image, self.rect)