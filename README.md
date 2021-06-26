# PokemonCardGame2021
(written by Rachelle)
This is a project done by Luxan and Rachelle regarding creating a cooperative coding project. This program is a virtual pokemon game, similar to pokemon card battles.
This program will be interacted with by using number inputs. All decisions will either have a number value assigned, or be directly for a number value. A database will be used to store available pokemon, which can be accesed from the main menu. When entering inputs, ensure there are no spaces, or other characters present. Interger values are the only accepted values.

This program consists of four main files; main, database, ASCII, and game components. The main file contains the while loop of the game. The database allows a user to edit the pokemon database, as well as contains functions to access database information. The ASCII file contains all ASCII's used in the program, as well as functions for ASCII movement. The game components file includes all functions used for the game to function, and calls to print information to the console.

The imports used in this program are as follows: random, os, pygame (mixer only), sqlite3, sys, time, and termcolor (colored only)
The pokemon background music was custom made by Rachelle, using Chrome Music Lab.

This program is written in python, and uses the console to share information with the user.
At any time the game can be quit by pressing cntl+c. In the main menu screen, the program can be closed by cntl+c as well.

If using pycharm to run this code the os clearing code will not function the way it does in repl (where this was coded)
Repl does not support music, but regardless both will run the program properly

For use of program without a database, replace the game loop file with the mainTest file
When using the mainTest file the only documents needed are asciiList, game components, the mainTest code and the music file
