import pygame as pg
from pygame.locals import *
from collections import deque
from bullet import Bullet

class Gun:
    def __init__(self, window, loc, image, nbullets, players):
        self.window = window
        self.nbullets = nbullets
        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, (200, 160))
        self.image_flipped = pg.transform.flip(self.image, 0, 1)
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.odds = [0.5, 0.5]
        self.bullets = self.load()
        self.players = players
        self.target = 0

    def load(self):
        bullets = deque()
        for _ in range(self.nbullets):
            bullets.append(Bullet(self.odds))
        return bullets
    
    def fire(self):
        return self.players[self.target], self.bullets.pop()
    
    def aimRight(self):
        self.target = not self.target
    
    def aimLeft(self):
        self.target = not self.target
            
    def update(self):
        print("Current bullets: ", [bullet.type for bullet in self.bullets])

    def draw(self):
        if self.target:
            self.window.blit(self.image_flipped, self.rect)
        else:
            self.window.blit(self.image, self.rect)