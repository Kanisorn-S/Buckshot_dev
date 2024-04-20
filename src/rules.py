import pygame as pg
from pygame.locals import *
import pygwidgets as pw
import sys
import random
from src.player import Player
from src.gameManager import GameManager
from src.new_scrollbar import ScrollText

# Set const parameters
WIDTH = 600
HEIGHT = 375
FRAMES_PER_SECOND = 60
NPLAYER = 2


# Load necessary images
background = pg.image.load('images/background.jpg')
raw_text = "1. Players start the game with 6 health, 4 healthy and 2 critical\n2. Players will take turns to shoot each other with the green box indicating the turn\n3. The amount of live and blank rounds will show on screen\n4. When shooting, players will have the choice to shoot the opponent or themselves\n5. Turns will switch after shooting an opponent or shooting yourself with a live round\n6. Player will continue their turn when shooting themselves with a blank round\n7. Shooting anyone will a live round will reduce their health by 1 point\n8. When out of bullets, the gun will reload and bullets will display again\n9. When all healthy health are gone player will enter the disrepair state \n    where they cannot gain health and will die on the next shot\n10. When one player dies, the other wins"

    

def rule_menu() -> int:
    clock = pg.time.Clock()
    window = pg.display.get_surface()
    backToMenuButton = pw.CustomButton(window, (300, 300), 'images/exit.png')
    backToMenuButton.setCenteredLoc((300, 335))
    scrollText = ScrollText(window, raw_text, (500, 200), (20, 20))
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if backToMenuButton.handleEvent(event):
                return 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    pg.display.toggle_fullscreen()
            scrollText.handleEvent(event)
            
        scrollText.update()

        window.blit(background, (0, 0))

        scrollText.draw()
        backToMenuButton.draw()
        
        pg.display.update()
        clock.tick(60)
        
            
    
        
    