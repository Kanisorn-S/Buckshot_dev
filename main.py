# Import Libs
import pygame as pg
from pygame.locals import *
import pygwidgets as pw
import sys
from src.gameManager import GameManager
from src.item import Item
from src.player import Player
from src.gun import Gun
from src.starting import starting_menu
from src.ending import ending_menu
from src.rules import rule_menu


# Set const parameters
WIDTH = 600
HEIGHT = 375
FRAMES_PER_SECOND = 60
NPLAYER = 2
NBULLETS = 6

logo = pg.image.load('images/heal.png')
# Initialize pygame
pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT), RESIZABLE | SCALED)
pg.display.set_caption("Buckshot Roulette")
pg.display.set_icon(logo)
clock = pg.time.Clock()

# Initialize mixer for music and sound effects
pg.mixer.init()
startMenuMusic = pg.mixer.Sound('sounds/record-online-voice-recorder_kIwejRI.mp3')
gameMusic = pg.mixer.Sound('sounds/Undertale_OST__095_-_Bring_It_In_Guys.mp3')
endMusic = pg.mixer.Sound('sounds/Victory Crew.mp3')

startMenuChannel = pg.mixer.Channel(0)
gameChannel = pg.mixer.Channel(1)
endChannel = pg.mixer.Channel(2)

gameChannel.set_volume(0.1)
startMenuChannel.set_volume(0.3)
endChannel.set_volume(0.3)

# Load necessary images
background = pg.image.load('images/background.jpg')
player1_full = pg.image.load('images/player1_full.png')
player1_red = pg.image.load('images/player1_red.png')
player1_eva = pg.image.load('images/player1_eva.png')
player2_full = pg.image.load("images/player2_full.png")
player2_red = pg.image.load("images/player2_red.png")
player2_eva = pg.image.load("images/player2_eva.png")
player_pics = [player2_full, player2_red, player2_eva, player1_full, player1_red, player1_eva]


# Application state for different menu
state = 0
started = False
gameStarted = False
endStarted = False


# Main program loop
while True:
    # check events
    if state == 0: # Starting Menu
        if not started:
            endChannel.fadeout(3000)
            endChannel.stop()
            startMenuChannel.play(startMenuMusic, loops = -1, fade_ms = 3000)
            started = True
        state = starting_menu()
    elif state == 2: # Ending Menu
        if not endStarted:
            endChannel.play(endMusic, loops = 0, fade_ms = 1000)
            endStarted = True
        state = ending_menu(gameManager)
    elif state == 3: # Rule Menu
        state = rule_menu()
    else:
        if not gameStarted:
            # Initialize GameManager
            gameManager = GameManager(window, player_pics, NBULLETS)
            started = False
            endStarted = False
            startMenuChannel.fadeout(3000)
            startMenuChannel.stop()
            endChannel.fadeout(3000)
            endChannel.stop()
            gameChannel.play(gameMusic, loops = -1, fade_ms = 3000)
            gameStarted = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if gameManager.winner == None:
                # Let game manager handle the event
                gameManager.handleEvent(event)

            
        # Frame update
        gameManager.update()
        if gameManager.winner:
            gameChannel.fadeout(2000)
            gameChannel.stop()
            gameStarted = False
            state = 2


            

        # Fill window's Background
        window.blit(background, (0, 0))

        gameManager.draw()

        pg.display.update()
        clock.tick(FRAMES_PER_SECOND)

    
    
    