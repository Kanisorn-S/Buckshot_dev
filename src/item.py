
import pygame as pg
from pygame.locals import *

class Item():
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
    def __init__(self, x, y, width, height, text, font, action):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.font = font
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
        color = (0, 255, 0) if self.active else (255, 0, 0)
        pg.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)















class PotOfGreed(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Draw 2 cards"
        self.image = pg.image.load("pot_of_greed.png")  
        self.rect = self.image.get_rect()

    def usedItem(self, Player, gun):
        #draw 2 items
        #Itemstack.loadItem(2)
        


class SuperCharger(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Next shot deals 2 damage"
        self.image = pg.image.load("super_charger.png")  
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
       #increase bullet damage
       gun.damage += 2 
       # one turn



class GNDrive(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Increase evasiveness by 50% for next shot"
        self.image = pg.image.load("gn_drive.png")  
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        player.evading = True
       #increase evasiveness
       


class DemonCore(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Skip opponent's turn (once per turn)"
        self.image = pg.image.load("demon_core.png") 
        self.rect = self.image.get_rect()
        self.used = False

    def usedItem(self, player, gun):
        if self.used == True:
            #draw new casd
            pass
        
        else:
            #skip opponent 1  turn
            pass



class Crewmate(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Restore one healthy heart to user"
        self.image = pg.image.load("crewmate.png")
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        # restore healty heart to player
        player.heath += 2
        
        pass


class AccessCard(Item):
    def __init__(self):
        super().__init__()
        self.effect = "Skip next shot and reveal bullet type"
        self.image = pg.image.load("access_card.png")  
        self.rect = self.image.get_rect()

    def usedItem(self, player, gun):
        #skip next shot and show that bullet type
        gun.skip_next_shot = True
        


class Lasso(Item):
    def __init__(self):
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


