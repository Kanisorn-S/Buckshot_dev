import pygame as pg
from pygame.locals import *
import pygwidgets as pw
from src.player import Player
from src.gun import Gun
from abc import ABC, abstractmethod

pg.mixer.init()
itemChannel = pg.mixer.Channel(5)
itemChannel.set_volume(0.1)
superChannel = pg.mixer.Channel(6)
superChannel.set_volume(0.3)
demonChannel = pg.mixer.Channel(7)
demonChannel.set_volume(0.04)
# highChannel = pg.mixer.Channel(8)
# highChannel.set_volume(0.6)

access_card = pg.mixer.Sound('sounds\Credit card sfx.mp3')
demon_core = pg.mixer.Sound('sounds\Demon core sfx.mp3')
gn_drive = pg.mixer.Sound('sounds\GN drive sfx.mp3')
pot_of_greed = pg.mixer.Sound('sounds\Pot of greed sfx.mp3')
super_charger = pg.mixer.Sound('sounds\Super Charger sfx.mp3')
heal = pg.mixer.Sound('sounds\Heal_sfx.mp3')
lasso = pg.mixer.Sound('sounds\Steal_sfx.mp3')

class Item(pw.CustomButton, ABC): # pw.CustomButton -> Inheretance, ABC -> abstraction
    def __init__(self, window: pg.Surface, image: str):
        super().__init__(window, (0, 0), image)
        self.blur = []
        self.imageForBlur = pg.image.load(image)
        for i in range(1, 6):
            self.blur.append(pg.transform.box_blur(self.imageForBlur, i))
        self.isActive = True
        self.current_sprite = 0
        self.timer = 0
        self.displaying = True
    
    def isUsed(self) -> bool:
        return not self.displaying

    @abstractmethod 
    def usedItem(self, player: Player, gun: Gun):
        pass
    
    def update(self):
        if not self.isActive:
            self.timer += 1
            if self.timer > 3:
                self.timer = 0
                if self.current_sprite >= 4:
                    self.displaying = False
                    self.disable()
                self.current_sprite += 1
    
    def draw(self):
        if self.isActive:
            super().draw()
        elif self.displaying:
            self.window.blit(self.blur[self.current_sprite], self.loc)
    
    def remove(self):
        self.isActive = False






class PotOfGreed(Item):
    pot_of_greed = 'images/pot_of_greed.png' # Class variable
    def __init__(self, window: pg.Surface):
        super().__init__(window, PotOfGreed.pot_of_greed)
        self.effect = "Draw 2 cards"


    def usedItem(self, player: Player, gun: Gun):
        #draw 2 items
        itemChannel.play(pot_of_greed, loops = 0)
        return 0
        


class SuperCharger(Item):
    power_amp = 'images/power_amp.png'
    def __init__(self, window: pg.Surface):
        super().__init__(window, SuperCharger.power_amp)
        self.effect = "Next shot deals 2 damage"


    def usedItem(self, player: Player, gun: Gun):
       # increase bullet damage
       superChannel.set_volume(1.8)
       superChannel.play(super_charger, loops = 0)
       gun.bullets[gun.bulletsLeft() - 1].damage = 2


class GNDrive(Item):
    evasiveness = 'images/evasiveness.png'
    def __init__(self, window: pg.Surface):
        super().__init__(window, GNDrive.evasiveness)
        self.effect = "Increase evasiveness by 0.5 for next shot"


    def usedItem(self, player: Player, gun: Gun):
        # player evasiveness to 0.5
        superChannel.set_volume(0.3)
        superChannel.play(gn_drive, loops = 0)
        player.evade()
        player.evasiveness = 0.5


class DemonCore(Item):
    skip = 'images/skip.png'
    def __init__(self, window: pg.Surface):
        super().__init__(window, DemonCore.skip)
        self.effect = "Skip opponent's turn (once per turn)"
        self.used = False

    def usedItem(self, player: Player, gun: Gun):
        demonChannel.play(demon_core, loops = 0)
        return 1



class Heal(Item):
    heal = 'images/heal.png'
    def __init__(self, window: pg.Surface):
        super().__init__(window, Heal.heal)

    def usedItem(self, player: Player, gun: Gun):
        # restore healty heart to player
        superChannel.set_volume(0.3)
        superChannel.play(heal, loops = 0)
        if not player.isDisrepair():
            player.health += 1
        


class AccessCard(Item):
    reload = 'images/reload.png'
    def __init__(self, window: pg.Surface):
        super().__init__(window, AccessCard.reload)

    def usedItem(self, player: Player, gun: Gun):
        # skip next shot and show that bullet type
        itemChannel.play(access_card, loops = 0)
        gun.eject()


class Lasso(Item):
    steal = 'images/steal.png'
    def __init__(self, window: pg.Surface):
        super().__init__(window, Lasso.steal)

    def usedItem(self, player: Player, gun: Gun):
        #take away one item on opponent side and destroy it
        superChannel.set_volume(0.3)
        superChannel.play(lasso, loops = 0)
        return 2

