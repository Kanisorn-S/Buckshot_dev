
import pygame as pg
from pygame.locals import *

class Item:
    def __init__(self):
        self.isActive = True
        self.image = None  # Placeholder for the item's image
        self.rect = None   # Placeholder for the item's rectangular area
        self.effect = None  # Placeholder for the effect the item has when used
        self.button = None  # Placeholder for the item's button

    def handleEvent(self, event):
        # Handle events for the button
        if self.button:
            self.button.handle_event(event)

    def usedItem(self, player, gun):
        pass

    def update(self):
        # Update the state of the button
        if self.button:
            self.button.update()

    def draw(self, screen):
        # Draw the button on the screen
        if self.isActive:
            screen.blit(self.image, self.rect)
            if self.button:
                self.button.draw(screen)

class Button:
    def __init__(self, x, y, image, action):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action
        self.active = True

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.active:
                    self.action()

    def update(self):
        # Update the state of the button
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class PotOfGreed(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Draw 2 cards"
        self.image = pg.image.load("pot_of_greed.png")  
        self.rect = self.image.get_rect()
        self.button = Button(0, 0, self.image, self.usedItem)

    def usedItem(self, Player, gun):
        # Draw 2 items
        # ItemStack.loadItem(2)
        pass

class SuperCharger(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Next shot deals 2 damage"
        self.image = pg.image.load("super_charger.png")  
        self.rect = self.image.get_rect()
        self.button = Button(0, 0, self.image, self.usedItem)

    def usedItem(self, player, gun):
       # Increase bullet damage
       gun.damage += 2 
       # One turn
       pass

class GNDrive(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Increase evasiveness by 50% for next shot"
        self.image = pg.image.load("gn_drive.png")  
        self.rect = self.image.get_rect()
        self.button = Button(0, 0, self.image, self.usedItem)

    def usedItem(self, player, gun):
        player.evading = True
       # Increase evasiveness

class DemonCore(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Skip opponent's turn (once per turn)"
        self.image = pg.image.load("demon_core.png") 
        self.rect = self.image.get_rect()
        self.used = False
        self.button = Button(0, 0, self.image, self.usedItem)

    def usedItem(self, player, gun):
        if self.used == True:
            # Draw new card
            pass
        else:
            # Skip opponent's turn
            pass

class Crewmate(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Restore one healthy heart to user"
        self.image = pg.image.load("crewmate.png")
        self.rect = self.image.get_rect()
        self.button = Button(0, 0, self.image, self.usedItem)

    def usedItem(self, player, gun):
        # Restore healthy heart to player
        player.heath += 2
        pass

class AccessCard(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Skip next shot and reveal bullet type"
        self.image = pg.image.load("access_card.png")  
        self.rect = self.image.get_rect()
        self.button = Button(0, 0, self.image, self.usedItem)

    def usedItem(self, player, gun):
        # Skip next shot and show bullet type
        gun.skip_next_shot = True
        pass

class Lasso(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Take away opponent's item"
        self.image = pg.image.load("lasso.png")  # Load image for Lasso
        self.rect = self.image.get_rect()
        self.button = Button(0, 0, self.image, self.usedItem)

    def usedItem(self, player, gun):
        # Take away one item from opponent's side and destroy it
        if player.opponent and player.opponent.item_stack:
            taken_item = player.opponent.item_stack.pop()
            print(f"Player {player.name} used Lasso! They took away {taken_item} from their opponent.")
        else:
            print(f"Player {player.name} used Lasso! But there is no item to take from the opponent.")
        pass
