import pygame as pg
from pygame.locals import *
from collections import deque
from src.player import Player
from src.bullet import Bullet

pg.mixer.init()
laser = pg.mixer.Sound('sounds\laser-104024.mp3')
laserChannel = pg.mixer.Channel(0)

class Gun:
    # Class Constants
    BLANK_IMG = pg.transform.scale_by(pg.image.load('images/blank_shot.png'), 0.02)
    LIVE_IMG = pg.transform.scale_by(pg.image.load('images/live_shot.png'), 0.02)
    BLANK_BLUR = []
    LIVE_BLUR = []
    for i in range(1, 6):
        BLANK_BLUR.append(pg.transform.box_blur(BLANK_IMG, i))
        LIVE_BLUR.append(pg.transform.box_blur(LIVE_IMG, i))
    IMG_W = LIVE_IMG.get_size()[0]
    
    def __init__(self, window: pg.Surface, loc: tuple[int, int], nbullets: int, players: list[Player, Player]):
        '''
        Initialize a cannon.
        Input : window - The main window display of the game
                loc - The center location of the gun
                nbullets - The number of bullets loaded into the gun
                players - A list of players in the game
        '''
        # Normal initialization
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
        self.players = players
        
        # Initialize bullets and firing mechanism
        self.odds = [0.5, 0.5] # [blank, live]
        self.bullets = self.load()
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
        self.hit = False
        self.phlive = self.live
        self.phblank = self.blank
        
        self.displaying = True
        self.displayingTimer = 0
        self.fading = False
        self.fadingTimer = 0
        self.fadeUpdate = 0
        self.blur_sprite = 0
        self.dx = 5
        self.live_img = Gun.LIVE_IMG
        self.blank_img = Gun.BLANK_IMG

    def load(self):
        '''
        Load the gun by initializing a stack of bullets with the odds of self.odds
        '''
        bullets = deque()
        for _ in range(self.nbullets):
            bullets.append(Bullet(self.window, self.odds))
        return bullets
    
    def fire(self) -> tuple[Player, Bullet]:
        '''
        Fire the gun. Returns the player and the bullet that was shot
        '''
        bullet = self.bullets.pop()
        bullet.aiming = self.target
        if bullet.type == Bullet.LIVE:
            self.live -= 1
        else:
            self.blank -= 1
        laserChannel.play(laser)
        return self.players[self.target], bullet
    
    def aimRight(self):
        '''
        Turns the gun to the right, update target and activate turning sequence sprite
        '''
        if self.target == 1:
            return
        self.turning_right = True
        self.target = 1
    
    def aimLeft(self):
        '''
        Turns the gun to the left, update target and activate turning sequence sprite
        '''
        if self.target == 0:
            return
        self.turning_left = True
        self.target = 0
            
    def update(self):
        '''
        Update the attributes of the gun, run turning sequence
        '''
        if self.fading:
            self.fadeUpdate += 1
            if self.fadeUpdate >= 15:
                self.fadeUpdate = 0
                if self.blur_sprite < len(Gun.BLANK_BLUR) - 1:
                    self.blur_sprite += 1
                else:
                    self.fading = False
                    self.displaying = False
        for bullet in self.bullets:
            bullet.aiming = self.target
            bullet.update()
        if self.hit:
            self.live = self.phlive
            self.blank = self.phblank
            self.hit = False
        if len(self.bullets) == 0:
            self.bullets = self.load()
            self.live = 0
            self.blank = 0
            for bullet in self.bullets:
                if bullet.type == Bullet.LIVE:
                    self.live += 1
                else:
                    self.blank += 1
            self.displaying = True
            self.displayingTimer = 0
            self.fading = False
            self.fadeUpdate = 0
            self.blur_sprite = 0
            self.live_img = Gun.LIVE_IMG
            self.blank_img = Gun.BLANK_IMG
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
        '''
        Draw the gun on the main game window
        '''
        self.window.blit(self.image, self.rect)
        if self.displaying:
            self.displayingTimer += 1
            if self.displayingTimer > 150:
                self.fading = True
                self.live_img = Gun.LIVE_BLUR[self.blur_sprite]
                self.blank_img = Gun.BLANK_BLUR[self.blur_sprite]
                
            x = 300
            y = 330
            factor = self.fading * ((-1) ** (self.fadeUpdate % 2) * self.dx)
            for i in range(self.live):
                rect = self.live_img.get_rect()
                rect.topright = (x - (i * Gun.IMG_W) + factor, y)
                self.window.blit(self.live_img, rect)
            for i in range(self.blank):
                rect = self.blank_img.get_rect()
                rect.topleft = (x + (i * Gun.IMG_W) + factor, y)
                self.window.blit(self.blank_img, rect)

    # Have an instance variable to keep track of the state of showing or hiding bullets
    # Fade bullets pic in/out