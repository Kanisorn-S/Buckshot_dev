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
- `main.py` - The main program, used to control which menu to display
- `gameManager.py` - GameManager class. Manage all elements of the game by initializing, updating, and drawing all elements
- `player.py` - Player class representing a player. Contains attributes like health, evasiveness, id and methods like shot, which updates the player's status after getting shot, and update, which facilitates the player's animation and sprite changes
- `gun.py` - Gun class representing the laser cannon. Contains a stack of `Bullet`s. Handle the aiming, shooting mechanisms and displaying of bullets.
- `bullet.py` - Bullet class representing a bullet. Contains class variables to signified its type, LIVE or BLANK. Contains the bullet's damage which is used to calculate a player's health after getting shot.
- `itemStack.py` - ItemStack class representing a deck of `Item`s to be drawn from. Manages and loads item randomly.
- `item.py` - Item abstsraction class, inherits from the pygwidgets.CustomButton class for functionality. Also contains different type of items as a subclass of the Item class, each differing in the usedItem method.
- `starting.py`, `ending.py`, `rules.py` - Contains functions that display different menus. Return an int that signifies the program's state, which is used by `main.py` to correctly display different menus
### How it works
- `main.py` - Display the correct menu by running different functions based on the current state of the program. Check for button press to change state by utilizing the pygwidgets.CustomButton.handleEvent method. Initializes a gameManager when in game state and passes events into the GameManager.handleEvent method
- `GameManager` - Initializes players using the loadPlayer method, a gun, and an itemStack. Keep tracks of each player's items in the playersItem attribute, the current turn, winner, target, and each object's status and makes appropriate update in the update method. Handles user's input, including aiming the gun, firing, and using items, throught the handleEvent method. Draws all the appropriate objects using the draw method
- `Player` - Have health, id, evading, evasiveness, disrepair as attributes. Contains getter and setter methods for health and evasiveness to employ data validation. The evade and shot methods are used to update the player's status when using the evasive item and getting shot respectively. The update and draw methods are used to do per-frame update and blit
- `Gun` - Have a list of players and target as attributes to keep track of the player who's being aimed at. The odds attribute is used , when loading bullets into the bullets attribute through the load method, to set the odds of a bullet being either live or blank, with the live and blank attribute keeping track of how many bullets of each type is left. Has the aimRight, aimLeft, and fire method for implementing the aiming and firing mechanism
- `Bullet` - Have type and damage as attribute to determine its effect on a player. The rest of the attributes and methods are for the firing animation
- `ItemStack` - Load a stack of items, using the loadItem method, into the items attribute on initialization. The getItem method is used to pop the top most item and the shuffle method shuffles the deck
- `Item` - An abstract class that inherits from pygwidget's CustomButton. Utilizes the CustomButton's handleEvent method to check for item usage. Has the usedItem method, called when an item is clicked on, as an abstract method. The rest of the attributes and methods are used for animation
### OOP Concepts/Techniques
- `Encapsulation` - Several classes uses encapsulation by having private attributes, using the property decorator, having a getter and setter function in conjunction with raising Exceptions in order to ensure the validity of the attribute's value. For example, the Player class has health and evasiveness as private. The setter for health ensures that a player's health doesn't exceed a max of 6, while the setter for evasiveness ensures that a player's evasiveness is a probability, that is being between 0 and 1 inclusive. The Gun class's odds attribute also employ a similar data validation as the Player's evasiveness. Furthermore, the target attribute is private, with the setter checking that the target is either 0 (aiming at Player1) or 1 (aiming at Player2)
- `Abstraction` - The update method and many other methods concerning animations is an abstraction. By hiding complicated details of updating the class's attributes, state, and sprite (for animation), the client program, the gameManager in this case, can simply call the update method without worrying about its complexity in its implementation
- `Inheritance` - The Item class and its subclasses exhibit inheritance. The Item class inherits from pygwidgets's CustomButton in order to utilize the functionality of a button, while adding additional methods for applying an item's effect. The different items then inherits from the item class, creating a class hierarchy. Each item modifies the usedItem method in order to implement its own functionality
- `Abstract Class` - By inheriting from ABC, the Item class is an abstract class. An Item object should never be initialized, only its subclass should. The item class also includes an abstract method: usedItem. Each item type must overrides this method in order to implement its own effect
- `Polymorphism` - Every class, except the ItemStack, exhibits polymorphism by having both the update and draw method. This allows the gameManager to call update and draw on every object in the program without worrying about its class. The different items also exhibits polymorphism through the usedItem method. Each item has a different implementation of the usedItem method in order to reflect the difference in effect; however, due to polymorphism, the gameManager can call usedItem on any item object


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.