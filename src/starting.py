import pygame as pg
from pygame.locals import *
import pygwidgets as pw
import sys
import random

# Set const parameters
WIDTH = 600
HEIGHT = 375
FRAMES_PER_SECOND = 60
NPLAYER = 2


# Load necessary images
background = pg.image.load('images/background.jpg')
logo = pg.image.load('images/logo.png')
logo = pg.transform.scale_by(logo, 0.5)
logo_mask = pg.mask.from_surface(logo).to_surface()
logo_mask.set_colorkey((0, 0, 0))
red = pg.image.load('images/amongus/red.png')
black = pg.image.load('images/amongus/black.png')
brown = pg.image.load('images/amongus/brown.png')
cyan = pg.image.load('images/amongus/cyan.png')
green = pg.image.load('images/amongus/green.png')
purple = pg.image.load('images/amongus/purple.png')
yellow = pg.image.load('images/amongus/yellow.png')
sus_images = [red, black, brown, cyan, green, purple, yellow]
sus_images = [pg.transform.scale(color, (60, 60)) for color in sus_images]


class Amongus:
    def __init__(self, window: pg.Surface, image: pg.Surface):
        self.window = window
        self.image = image
        self.rect = image.get_rect()
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        self.rect.center = (x, y)
        self.x_speed = random.choice([-2, -1, 1, 2])
        self.y_speed = random.choice([-2, -1, 1, 2])
        self.angle = 0
        self.rw = self.rect.w
        self.rh = self.rect.h
        self.omega = random.randint(-10, 10) | 1
        
    def update(self):
        
        if (self.rect.center[0] - self.rw / 2)  < 0:
            self.rect.centerx = self.rw / 2 + 2
            self.x_speed = -self.x_speed
        if (self.rect.center[0] + self.rw / 2) > WIDTH:
            self.rect.centerx = WIDTH - self.rw / 2 - 2
            self.x_speed = -self.x_speed
        if (self.rect.center[1] - self.rh / 2) < 0:
            self.rect.centery = self.rh / 2 + 2
            self.y_speed = -self.y_speed
        if (self.rect.center[1] + self.rh / 2) > HEIGHT:
            self.rect.centery = HEIGHT - self.rh / 2 - 2
            self.y_speed = -self.y_speed
        self.angle += self.omega
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
               
        
        
    def rotate(self) -> pg.Surface:
        return pg.transform.rotate(self.image, self.angle)
        
    def draw(self):
        image = self.rotate()
        image_rect = image.get_rect()
        image_rect.center = self.rect.center
        self.rw, self.rh = image_rect.size
        self.window.blit(image, image_rect)
    

def starting_menu() -> int:
    clock = pg.time.Clock()
    window = pg.display.get_surface()
    startButton = pw.TextButton(window, (300, 300), 'START')
    startButton.setCenteredLoc((300, 300))
    logo_rect = logo.get_rect()
    logo_rect.center = (300, 100)
    susses = [Amongus(window, color) for color in sus_images]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if startButton.handleEvent(event):
                return 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    pg.display.toggle_fullscreen()
        
        
        window.blit(background, (0, 0))
        for sus in susses:
            sus.update()
            sus.draw()
        window.blit(logo_mask, (logo_rect.x + 2, logo_rect.y + 2))
        window.blit(logo, logo_rect)

        startButton.draw()

        
        pg.display.update()
        clock.tick(60)
        
            
    
        
    