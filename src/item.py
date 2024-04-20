


import pygame as pg
from pygame.locals import *

class Item():
    def __init__(self):
        self.isActive = True
        self.image = None  # Placeholder for the item's image
        self.rect = None   # Placeholder for the item's rectangular area
        self.effect = None  # Placeholder for the effect the item has when used

    def handleEvent(self, e):
        #create button and receive button click
        pass
    
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
    def __init__(self):
        super().__init__()
        self.effect = "Draw 2 cards"
        self.image = pg.image.load("pot_of_greed.png")  # Load image for Pot of Greed
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        # Implement the functionality of Pot of Greed
        pass


class SuperCharger(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Next shot deals 2 damage"
        self.image = pg.image.load("super_charger.png")  # Load image for Super Charger
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        # Implement the functionality of Super Charger
        pass


class GNDrive(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Increase evasiveness by 50% for next shot"
        self.image = pg.image.load("gn_drive.png")  # Load image for GN Drive
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        # Implement the functionality of GN Drive
        pass


class DemonCore(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Skip opponent's turn (once per turn)"
        self.image = pg.image.load("demon_core.png")  # Load image for Demon Core
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        # Implement the functionality of Demon Core
        pass


class Crewmate(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Restore one healthy heart to user"
        self.image = pg.image.load("crewmate.png")  # Load image for Crewmate
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        # Implement the functionality of Crewmate
        pass


class AccessCard(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Skip next shot and reveal bullet type"
        self.image = pg.image.load("access_card.png")  # Load image for Access Card
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        # Implement the functionality of Access Card
        pass


class Lasso(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Take away opponent's item"
        self.image = pg.image.load("lasso.png")  # Load image for Lasso
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        # Implement the functionality of Lasso
        pass