import pygame as pg
from pygame.locals import *
import pygwidgets as pw

class Item(pw.CustomButton):
    def __init__(self, window, loc, image):
        super().__init__(window, loc, image)
        self.isActive = True
        self.image = None  # Placeholder for the item's image
        self.rect = None   # Placeholder for the item's rectangular area
        self.effect = None  # Placeholder for the effect the item has when used
    
    def usedItem(self, player, gun):
        pass

    def update(self):
        pass
        #update the state

    def draw(self, screen):
        #show on screen
        if self.isActive:
            screen.blit(self.image, self.rect)


class PotOfGreed(Item):
    pot_of_greed = 'images/pot_of_greed'
    def __init__(self, window, loc):
        super().__init__(window, loc, PotOfGreed.pot_of_greed)
        self.effect = "Draw 2 cards"
        self.image = pg.image.load("pot_of_greed.png")  # Load image for Pot of Greed
        self.rect = self.image.get_rect()

    def usedItem(self, Player, gun):
        #draw 2 items
        self.heath += 1
        


class SuperCharger(Item):
    power_amp = 'images/power_amp.png'
    def __init__(self, window, loc):
        super().__init__(window, loc, SuperCharger.power_amp)
        self.effect = "Next shot deals 2 damage"
        self.image = pg.image.load("super_charger.png")  # Load image for Super Charger
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
       #increase bullet damage
       gun.damage += 2 
       # one turn


class GNDrive(Item):
    evasiveness = 'imgaes/evasiveness.png'
    def __init__(self, window, loc):
        super().__init__(window, loc, GNDrive.evasiveness)
        self.effect = "Increase evasiveness by 0.5 for next shot"
        self.image = pg.image.load("gn_drive.png")  # Load image for GN Drive
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        player.evading = True
       #increase evasiveness
        pass


class DemonCore(Item):
    skip = 'images/skip.png'
    def __init__(self, window, loc):
        super().__init__(window, loc, DemonCore.skip)
        self.effect = "Skip opponent's turn (once per turn)"
        self.image = pg.image.load("demon_core.png")  # Load image for Demon Core
        self.rect = self.image.get_rect()
        self.used = False

    def usedItem(self, player, gun):
        if self.used == True:
            #draw new casd
            pass
        
        else:
            #skip opponent 1  turn
            pass



class Heal(Item):
    heal = 'images/heal.png'
    def __init__(self, window, loc):
        super().__init__()
        self.effect = "Restore one healthy heart to user"
        self.image = pg.image.load("crewmate.png")  # Load image for Crewmate
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        # restore healty heart to player
        player.heath += 2
        
        pass


class AccessCard(Item):
    def __init__(self, window, loc):
        super().__init__()
        self.effect = "Skip next shot and reveal bullet type"
        self.image = pg.image.load("access_card.png")  # Load image for Access Card
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        #skip next shot and show that bullet type
        gun.skip_next_shot = True
        pass


class Lasso(Item):
    def __init__(self, window, loc):
        super().__init__()
        self.effect = "Take away opponent's item"
        self.image = pg.image.load("lasso.png")  # Load image for Lasso
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        #take away one item on opponent side and destroy it
        if player.opponent:
            if player.opponent.item_stack:
                taken_item = player.opponent.item_stack.pop()
                print("Player {} used Lasso! They took away {} from their opponent.".format(player.name, taken_item))
            else:
                print("Player {} used Lasso! But their opponent has no items to take.".format(player.name))
        else:
            print("Player {} used Lasso! But there is no opponent to take an item from.".format(player.name))
        pass