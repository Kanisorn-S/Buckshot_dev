import pygame as pg
from pygame.locals import *
from src.gun import Gun 
from src.player import Player
from src.item import Item

class GameManager:
    def __init__(self, window : pg.Surface, nplayers: int, players_pic: pg.Surface, nbullets: int, gun : pg.Surface, itemframe: pg.Surface, heart: pg.Surface):
        '''
        Initialize the gameManager.
        Input : window - The main display window of the game
                nplayers - The number of players in the game
                players_pic - A list of tuple, each tuple containing a normal player pic and a green outlined player pic
                nbullets - The number of bullets in the gun
                gun - A loaded picture of the cannon
        Attributes : locations - A list of coordinates of the center of each players
                     playersInfo - A dictionary where the key is the player and the value is the player's health
                     players - A list of players
                     gun - The gun object 
                     turn - An int that is the index of the player whose turn it currently is
                     winner - None by default. It is set to a player when that player is the last man standing
        '''
        self.window = window
        self.nplayers = nplayers
        self.nbullets = nbullets
        self.players_pic = players_pic
        self.locations = [(100, 375/2), (500, 375/2)]
        self.playersInfo = self.loadPlayer()
        self.players = tuple(self.playersInfo.keys())
        self.gun = Gun(self.window, (330, 460/2), nbullets, self.players)
        self.turn = 0
        self.winner = None
        self.bullets_on_screen = []
        self.itemframes = []
        for i in range(4):
            image = pg.transform.scale_by(itemframe, 0.08)
            rect = image.get_rect()
            self.itemframes.append((image, rect))
        self.itemframes[0][1].center = (200, 375/4)
        self.itemframes[1][1].center = (400, 375/4)
        self.itemframes[2][1].center = (200, 3*375/4)
        self.itemframes[3][1].center = (400, 3*375/4)
        self.heart = pg.transform.scale_by(heart, 0.01)
        print(str(self.playersInfo))
        self.target = None
        
    def loadPlayer(self):
        '''
        Create nplayers Player and return a dictionary with the keys being players and the values being their corresponding health
        '''
        Players = {}
        for i in range(self.nplayers):
            player = Player(self.window, self.players_pic[i], self.locations[i], i, f"Player{i}")
            Players[player] = player.health
        return Players
    
    def handleEvent(self, e: pg.Event):
        if e.key == pg.K_SPACE:
            self.target, bullet = self.gun.fire()
            self.bullets_on_screen.append(bullet)
            bullet.fired()

            
            if self.target != self.players[self.turn]:
                self.turn = not self.turn
        elif e.key == pg.K_RIGHT:
            self.gun.aimRight()
        elif e.key == pg.K_LEFT:
            self.gun.aimLeft()
        
        if e.key == pg.K_f:
            pg.display.toggle_fullscreen()

    def update(self):
        '''
        Loop through all the players.
        Calls update on each player then update the health of each player in the playersInfo dictionary.
        If a player's health reaches zero, remove them from the game.
        Check if there's only one player standing, set them as the winner.
        Update the gun (run cannon reload annimation sprite)
        '''
        for player in self.players:
            player.update()
            self.playersInfo[player] = player.health
            if self.playersInfo[player] <= 0:
                del self.playersInfo[player]
            if player == self.players[self.turn]:
                player.isTurn = True
        if not len(self.playersInfo.keys()):
            self.winner = self.playersInfo.keys()[0]
        
        self.gun.update()
        for bullet in self.bullets_on_screen:
            if bullet.rect.colliderect(self.target.rect):
                # print('bullet removed')
                self.target.shot(bullet)
                self.gun.hit = True
                self.bullets_on_screen.remove(bullet)
            bullet.update()

    def draw(self):
        '''
        Draws all the components by calling draw() on all objects.
        If a winner is determined, show end screen.
        '''
        if self.winner is None:
            for player in self.players:
                player.draw()
                x, y = player.rect.topleft
                image = self.heart
                w, h = image.get_size()
                for i in range(self.playersInfo[player]):
                    rect = image.get_rect()
                    rect.bottomleft = (x + (i * w), y)
                    self.window.blit(image, rect)
            for bullet in self.bullets_on_screen:
                bullet.draw()
            for itemframe, rect in self.itemframes:
                self.window.blit(itemframe, rect)
            self.gun.draw()
        else:
            # show winning screen with victor at the center
            pass
