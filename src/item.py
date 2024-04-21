import pygame as pg
from pygame.locals import *
import pygwidgets as pw

class Item(pw.CustomButton):
    def __init__(self, window, image):
        super().__init__(window, (0, 0), image)
        self.isActive = True

    
    def usedItem(self, player, gun):
        print("Item is used")

    def update(self):
        pass
        #update the state



class PotOfGreed(Item):
    pot_of_greed = 'images/pot_of_greed.png'
    def __init__(self, window):
        super().__init__(window, PotOfGreed.pot_of_greed)
        self.effect = "Draw 2 cards"


    def usedItem(self, player, gun):
        #draw 2 items
        player.heath += 1
        


class SuperCharger(Item):
    power_amp = 'images/power_amp.png'
    def __init__(self, window):
        super().__init__(window, SuperCharger.power_amp)
        self.effect = "Next shot deals 2 damage"


    def usedItem(self, player, gun):
       #increase bullet damage
       gun.damage += 2 
       # one turn


class GNDrive(Item):
    evasiveness = 'images/evasiveness.png'
    def __init__(self, window):
        super().__init__(window, GNDrive.evasiveness)
        self.effect = "Increase evasiveness by 0.5 for next shot"


    def usedItem(self, player, gun):
        player.evading = True
       #increase evasiveness
        pass


class DemonCore(Item):
    skip = 'images/skip.png'
    def __init__(self, window):
        super().__init__(window, DemonCore.skip)
        self.effect = "Skip opponent's turn (once per turn)"
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
    def __init__(self, window):
        super().__init__(window, Heal.heal)

    def usedItem(self, player, gun):
        # restore healty heart to player
        player.heath += 2
        
        pass


class AccessCard(Item):
    reload = 'images/reload.png'
    def __init__(self, window):
        super().__init__(window, AccessCard.reload)

    def usedItem(self, player, gun):
        #skip next shot and show that bullet type
        gun.skip_next_shot = True
        pass


class Lasso(Item):
    steal = 'images/steal.png'
    def __init__(self, window):
        super().__init__(window, Lasso.steal)

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