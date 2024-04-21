# Starship Showdown

Starship Showdown is a fun and thrilling, space-themed, local multiplayer game adapted from "Buckshot Roulette" and implemented in Python using the Pygame library.

## Installation

You will need to download Python and some additional packages in order to run "Starship Showdown."

### Installing Python
Download and install Python from https://www.python.org/downloads/

### Installing Packages
#### Pygame
Run the following command in your terminal to install Pygame:
```bash
pip install pygame
```
#### Pygwidgets
Run the following command in your terminal to intsall Pygwidgets:
```bash
pip install pygwidgets
```
### Downloading the Game
You can download the files for Starship Showdown directly from this repository or use Git to clone the repository by running the following command in your terminal:
```bash
git clone https://github.com/Kanisorn-S/Buckshot_dev.git
```

## Usage

Navigate to the "Buckshot_dev" directory then run the following command in the terminal to start the program:
```bash
python main.py
```

## How to play
### Rules of the Game
1. Players start the game with 6 health, 4 healthy and 2 critical
2. Players will take turns to shoot each other with the green box indicating the turn
3. The amount of live and blank rounds will show on screen
4. When shooting, players will have the choice to shoot the opponent or themselves
5. Turns will switch after shooting an opponent or shooting yourself with a live round
6. Player will continue their turn when shooting themselves with a blank round
7. Shooting anyone will a live round will reduce their health by 1 point
8. When out of bullets, the gun will reload and bullets will display again
9. When all healthy health are gone player will enter the disrepair state where they cannot gain health and will die on the next shot
10. When one player dies, the other wins

### Items
1. Items are used to affect the games in your favor
2. Every time the gun is reloaded, each player will gain 4 random items which can be in duplicates
3. Each player can only have a total of 8 items at once and new items won’t be added
4. Items can only be used in the corresponding player’s turns

#### Items Available
1. `Pot of greed` - Gets 2 additional items
2. `Super charger` - The next shot will deal 2 points of damage 
3. `GN drive` - Increases the evasiveness of the user by 50% for the next shot taken
4. `Demon core` - Skips the opponent’s turn and can only be used once in the user’s turn
5. `Crewmate` - Restore one healthy heart of the user but will do nothing when in the disrepair state
6. `Access Card` - Immediately skip the next shot in the gun and show what type of bullet it is 
7. `Lasso` - Takes away one item on the opponent’s side and destroy it

### Basic Controls
- `Left/Right Arrow` - Aims the laser cannon
- `Spacebar` - Fire
- Click on items to use
- `F` - Toggle full screen mode


## Program Architecture
This project is developed as a part of the Programming Methodologies course, focusing on Object-Oriented Programming.
### Folder Structure
- `images` - Contains all of the artwork and sprites
- `sounds` - Contains all of the music and sound effects
- `src` - Contains all of the Class and Function code
### Important Files
- `main.py` 



## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.