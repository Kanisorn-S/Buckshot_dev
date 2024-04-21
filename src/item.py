import pygame as pg
from pygame.locals import *
import pygwidgets as pw

pg.mixer.init()
itemChannel = pg.mixer.Channel(5)
itemChannel.set_volume(0.2)

access_card = pg.mixer.Sound('sounds\Credit card sfx.mp3')
demon_core = pg.mixer.Sound('sounds\Demon core sfx.mp3')
gn_drive = pg.mixer.Sound('sounds\GN drive sfx.mp3')
pot_of_greed = pg.mixer.Sound('sounds\Pot of greed sfx.mp3')
super_charger = pg.mixer.Sound('sounds\Super Charger sfx.mp3')
heal = pg.mixer.Sound('sounds\Heal_sfx.mp3')
lasso = pg.mixer.Sound('sounds\Steal_sfx.mp3')

class Item(pw.CustomButton):
    def __init__(self, window, image):
        super().__init__(window, (0, 0), image)
        self.isActive = True

    
    def usedItem(self, player, gun):
        print("Item is used")
    
    def handleEvent(self, event):
        return False

    def update(self):
        pass
        #update the state

    def __del__(self):
        print("Item is gone")



class PotOfGreed(Item):
    pot_of_greed = 'images/pot_of_greed.png'
    def __init__(self, window):
        super().__init__(window, PotOfGreed.pot_of_greed)
        self.effect = "Draw 2 cards"


    def usedItem(self, player, gun):
        #draw 2 items
        itemChannel.play(pot_of_greed, loops = 0)
        return 0
        


class SuperCharger(Item):
    power_amp = 'images/power_amp.png'
    def __init__(self, window):
        super().__init__(window, SuperCharger.power_amp)
        self.effect = "Next shot deals 2 damage"


    def usedItem(self, player, gun):
       # increase bullet damage
       itemChannel.play(super_charger, loops = 0)
       gun.bullets[len(gun.bullets) - 1].damage = 2


class GNDrive(Item):
    evasiveness = 'images/evasiveness.png'
    def __init__(self, window):
        super().__init__(window, GNDrive.evasiveness)
        self.effect = "Increase evasiveness by 0.5 for next shot"


    def usedItem(self, player, gun):
        # player evasiveness to 0.5
        itemChannel.play(gn_drive, loops = 0)
        player.evading = True
        player.evasiveness = 0.5


class DemonCore(Item):
    skip = 'images/skip.png'
    def __init__(self, window):
        super().__init__(window, DemonCore.skip)
        self.effect = "Skip opponent's turn (once per turn)"
        self.used = False

    def usedItem(self, player, gun):
        itemChannel.play(demon_core, loops = 0)
        return 1



class Heal(Item):
    heal = 'images/heal.png'
    def __init__(self, window):
        super().__init__(window, Heal.heal)

    def usedItem(self, player, gun):
        # restore healty heart to player
        itemChannel.play(heal, loops = 0)
        if not player.disrepair:
            player.health += 1
        


class AccessCard(Item):
    reload = 'images/reload.png'
    def __init__(self, window):
        super().__init__(window, AccessCard.reload)

    def usedItem(self, player, gun):
        # skip next shot and show that bullet type
        itemChannel.play(access_card, loops = 0)
        gun.eject()


class Lasso(Item):
    steal = 'images/steal.png'
    def __init__(self, window):
        super().__init__(window, Lasso.steal)

    def usedItem(self, player, gun):
        #take away one item on opponent side and destroy it
        itemChannel.play(lasso, loops = 0)
        print("Player {} used Lasso! They took away from their opponent.".format(player.name))
        print("Player {} used Lasso! But their opponent has no items to take.".format(player.name))
        return 2

