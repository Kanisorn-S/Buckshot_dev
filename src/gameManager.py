import pygame as pg
from pygame.locals import *
from src.gun import Gun 
from src.player import Player
from src.item import Item
from src.itemStack import ItemStack
from src.bullet import Bullet

itemframe = pg.image.load('images/itembox.png')

class GameManager:
    def __init__(self, window : pg.Surface, players_pic: list[pg.Surface], nbullets: int):
        '''
        Initialize the gameManager.
        Input : window - The main display window of the game
                players_pic - A list of players' pic in different states
                nbullets - The number of bullets in the gun
        '''
        self.window = window
        self.nplayers = 2
        self.nbullets = nbullets
        self.players_pic = players_pic
        self.locations = [(70, 375/2), (530, 375/2)]
        self.players = []
        self.playersInfo = self.loadPlayer()
        self.playersItem = {player: [] for player in self.players}
        self.gun = Gun(self.window, (330, 460/2), nbullets, self.players)
        self.turn = 0
        self.winner = None
        self.bullets_on_screen = []

        # Itemframes
        self.itemframes = []
        for i in range(4):
            image = pg.transform.scale_by(itemframe, 0.08)
            rect = image.get_rect()
            self.itemframes.append((image, rect))
        self.itemframes[0][1].center = (200, 375/4)
        self.itemframes[1][1].center = (400, 375/4)
        self.itemframes[2][1].center = (200, 3*375/4)
        self.itemframes[3][1].center = (400, 3*375/4)
        self.target = None

        # Item management
        self.itemStack = ItemStack(self.window, 100)
        self.gotItem = False
        
        # Timer for death animation
        self.death_time = 0
        
    def loadPlayer(self):
        '''
        Create nplayers Player and return a dictionary with the keys being players and the values being their corresponding health
        '''
        Players = {}
        player1 = Player(self.window, self.players_pic[0:3], self.locations[0], 0, "Player 1")
        Players[player1] = player1.health
        self.players.append(player1)
        player2 = Player(self.window, self.players_pic[3:], self.locations[1], 1, "Player 2")
        Players[player2] = player2.health
        self.players.append(player2)
        return Players
    
    def handleEvent(self, e: pg.event):
        '''
        Handle events from the user's input
        '''
        if self.death_time:
            return
        if e.type == pg.KEYDOWN: 
        # Spacebar to fire
            if e.key == pg.K_SPACE:
                if self.gun.displaying:
                    return
                if self.gun.target not in [0, 1]:
                    return
                self.target, bullet = self.gun.fire()
                self.bullets_on_screen.append(bullet)
                bullet.fired()
                self.target.shot(bullet)

                # If fired at opponent or fired the last bullet, lose turn
                if (self.target != self.players[self.turn]) or (bullet.type == Bullet.LIVE) or not(len(self.gun.bullets)):
                    self.turn = not self.turn
                    self.gotItem = False
            
            # Change aim of the gun
            elif e.key == pg.K_RIGHT:
                self.gun.aimRight()
            elif e.key == pg.K_LEFT:
                self.gun.aimLeft()
            
            if e.key == pg.K_f:
                pg.display.toggle_fullscreen()
        
    def distributeItems(self):
        print("distributing items")
        for player in self.players:
            for _ in range(4):
                self.playersItem[player].append(self.itemStack.getItem())

    def update(self):
        '''
        Loop through all the players.
        Calls update on each player then update the health of each player in the playersInfo dictionary.
        If a player's health reaches zero, remove them from the game.
        Check if there's only one player standing, set them as the winner.
        Update the gun and bullets on screen.
        '''
        for player in self.players:
            player.update()
            self.playersInfo[player] = player.health
            if self.playersInfo[player] <= 0:
                self.death_time += 1
                if self.death_time >= 60:
                    del self.playersInfo[player]
                    self.players.remove(player)
                    self.winner = self.players[0]
                    break
            # if player == self.players[self.turn]:
            #     player.isTurn = True

        
        reload = self.gun.update()
        if reload:
            self.distributeItems()
        for bullet in self.bullets_on_screen:
            bullet.update()

    def draw(self):
        '''
        Draws all the components by calling draw() on all objects.
        If a winner is determined, show end screen.
        '''
        if self.winner is None:
            for player in self.players:
                player.draw()
            for bullet in self.bullets_on_screen:
                bullet.draw()
            for itemframe, rect in self.itemframes:
                self.window.blit(itemframe, rect)
            self.gun.draw(self.death_time)
            current_player = self.players[self.turn]
            if current_player.health > 0:
                pg.draw.rect(self.window, 'green', current_player.rect, 2, border_radius = 5)
        else:
            # show winning screen with victor at the center
            print(f"The winner is {self.winner.name}")
