import pygame as pg
from pygame.locals import *
from src.gun import Gun 
from src.player import Player
from src.item import Item
from src.itemStack import ItemStack
from src.bullet import Bullet
import random

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
        self.target = None

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


        # Item management
        self.itemStack = ItemStack(self.window, 100)
        
        # Timer for death animation
        self.death_time = 0

        self.itemPos1 = [(160, 45), (203, 45), (160, 88), (203, 88), (160, 235), (203, 235), (160, 278), (203, 278)]
        self.itemPos1 = [(w , h + 5) for w, h in self.itemPos1]
        self.nItems1 = 0
        self.slot1 = {i:0 for i in range(8)}
        self.itemPos2 = [(357, 45), (400, 45), (357, 88), (400, 88), (357, 235), (400, 235), (357, 278), (400, 278)]
        self.itemPos2 = [(w + 5, h + 5) for w, h in self.itemPos2]
        self.nItems2 = 0
        self.slot2 = {i:0 for i in range(8)}

        self.free_shot = False
        self.lock = False
        
    def loadPlayer(self):
        '''
        Create 2 Player and return a dictionary with the keys being players and the values being their corresponding health
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
            # Disable input when a player is killed
            return
        if e.type == pg.KEYDOWN: 
        # Spacebar to fire
            if e.key == pg.K_SPACE:
                if self.gun.isDisplaying():
                    return
                if self.gun.target not in [0, 1]:
                    return
                self.target, bullet = self.gun.fire()
                self.bullets_on_screen.append(bullet)
                bullet.fired()
                self.target.shot(bullet)

                # If fired at opponent or fired the last bullet, lose turn
                if ((self.target != self.players[self.turn]) or (bullet.type == Bullet.LIVE) or not(len(self.gun.bullets))) and ((not self.free_shot) or self.lock):
                    self.turn = not self.turn
                    self.lock = False
                elif (self.target != self.players[self.turn]) or (bullet.type == Bullet.LIVE) or not(len(self.gun.bullets)):
                    self.free_shot = False
                    self.lock = True
            
            # Change aim of the gun
            elif e.key == pg.K_RIGHT:
                self.gun.aimRight()
            elif e.key == pg.K_LEFT:
                self.gun.aimLeft()
            
            if e.key == pg.K_f:
                pg.display.toggle_fullscreen()
        
        for i, item in self.playersItem[self.players[self.turn]]:
            if self.gun.isDisplaying():
                return
            if item.handleEvent(e):
                result = item.usedItem(self.players[self.turn], self.gun)
                item.remove()
                if self.turn == 0:
                    self.slot1[i] = 0
                else:
                    self.slot2[i] = 0
                if result == 0: # Pot of greed
                    self.distributeItems(id = self.turn, amount = 2)
                elif result == 1: # Skip
                    self.free_shot = True
                elif result == 2: # Lasso
                    opp = not self.turn
                    stolen_slot = random.randint(0, 7)
                    if opp == 0:
                        j = 0
                        while self.slot1[stolen_slot] == 0:
                            if j > 6:
                                break
                            stolen_slot = (stolen_slot + 1) % 8
                            j += 1
                        for slot, item in self.playersItem[self.players[opp]]:
                            if slot == stolen_slot:
                                item.remove()
                                self.slot1[stolen_slot] = 0
                    else:
                        j = 0
                        while self.slot2[stolen_slot] == 0:
                            if j > 6:
                                break
                            stolen_slot = (stolen_slot + 1) % 8
                            j += 1
                        for slot, item in self.playersItem[self.players[opp]]:
                            if slot == stolen_slot:
                                item.remove()
                                self.slot2[stolen_slot] = 0
                        
        
    def distributeItems(self, id = 2, amount = 4):
        # Player1
        if id == 0 or id == 2:
            full1 = False
            added1 = 0
            for i in range(amount):
                slot = (self.nItems1 + i) % 8
                j = 0
                while self.slot1[slot]:
                    if j >=7:
                        full1 = True
                        break
                    slot = (slot + 1) % 8
                    j += 1
                if not full1:
                    self.playersItem[self.players[0]].append((slot, self.itemStack.getItem()))
                    self.slot1[slot] = 1
                    added1 += 1
                else:
                    break
            self.nItems1 += added1
        # Player2
        if id == 1 or id == 2:
            full2 = False
            added2 = 0
            for i in range(amount):
                slot = (self.nItems2 + i) % 8
                j = 0
                while self.slot2[slot]:
                    if j >=7:
                        full2 = True
                        break
                    slot = (slot + 1) % 8
                    j += 1
                if not full2:
                    self.playersItem[self.players[1]].append((slot, self.itemStack.getItem()))
                    self.slot2[slot] = 1
                    added2 += 1
                else:
                    break
            self.nItems2 += added2

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
            
        for i in range(len(self.players)):
            for slot, item in self.playersItem[self.players[i]]:
                item.update()
                if item.isUsed():
                    self.playersItem[self.players[i]].remove((slot, item))
                
                
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
            # Player 1
            for i, item in self.playersItem[self.players[0]]:
                item.setLoc(self.itemPos1[i])
                item.draw()
            # Player 2 
            for j, item in self.playersItem[self.players[1]]:
                item.setLoc(self.itemPos2[j])
                item.draw()

        else:
            # show winning screen with victor at the center
            print(f"The winner is {self.winner.name}")
