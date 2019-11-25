# Python text RPG #

import cmd
import textwrap
import sys
import os
import time
import random
import winsound
from playsound import playsound


screen_width = 100

############################################################################### Player setup ##############################################################################

class player:
    def __init__(self):
        self.name = "Erbag"
        self.job = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'a1'
        self.game_over = False

# Create player #
myPlayer = player()

################################################################################ Title screen #############################################################################

def title_screen_selections():
    option = input(">")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()

    while option.lower() not in ["play", "help", "quit"]:
        print("Please enter, 'play', 'help', or 'quit'.")
        option = input(">")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    goblin = """
             ,      ,\n
            /(.-""-.)\ \n
        |\  \/      \/  /| \n
        | \ / =.  .= \ / | \n
        \( \   o\/o   / )/ \n
         \_, '-/  \-' ,_/ \n
           /   \__/   \ \n
           \ \__/\__/ / \n
         ___\ \|--|/ /___\n
       /`    \      /    `\ \n
      /       '----'       \ \n
    """
    os.system("cls")
    winsound.PlaySound("music/song18(online-audio-converter.com).wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    print("########################")
    print("  Welcome to Bist Quest ")
    print(" " + goblin)
    print("########################")
    print("         -Play-         ")
    print("         -Help-         ")
    print("         -Quit-         ")
    title_screen_selections()

def help_menu():
    print("         -Use up down left right to move-         ")
    print("         -Type your commands-         ")
    print("         -Use 'Look' to inspect-         ")
    title_screen_selections()

#################################################################################### Game interactivity ##############################################################
def print_location():
    print("\n" + ('#' *(15 + len(myPlayer.location))))
    print("# " + myPlayer.location.upper() + ' #')
    print("# " + zonemap[myPlayer.location][ZONE_NAME] + " #")
    print("# " + zonemap[myPlayer.location][DESCRIPTION] + " #")
    print("\n" + ('#' *(15 + len(myPlayer.location))))
    playsound(zonemap[myPlayer.location][SOUND_EFFECT])



def prompt():
    print("\n" + "======================")
    print("What would you like to do?")
    action = input(">")
    acceptable_actions = ["move", "go", "travel", "walk", "quit", "examine", "inspect", "interact", "look"]
    while action.lower() not in acceptable_actions:
        print("You can't do this, try again")
        action = input(">")
    if action.lower() == "quit":
        sys.exit()        
    elif action.lower() in ["move", "go", "travel", "walk"]:
        playsound("music/walk.wav")
        playsound("music/walk2.wav")
        playsound("music/walk.wav")
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "interact", "look"]:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to travel?\n"
    destination = input(ask)
    if destination in ["up", "north"]:
        playsound("music/walk.wav")
        playsound("music/walk2.wav")
        playsound("music/walk.wav")
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    if destination in ["down", "south"]:
        playsound("music/walk.wav")
        playsound("music/walk2.wav")
        playsound("music/walk.wav")
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    if destination in ["left", "west"]:
        playsound("music/walk.wav")
        playsound("music/walk2.wav")
        playsound("music/walk.wav")
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    if destination in ["right", "east"]:
        playsound("music/walk.wav")
        playsound("music/walk2.wav")
        playsound("music/walk.wav")
        destination = zonemap[myPlayer.location][RIGHT]
        town_name  = zonemap[myPlayer.location][ZONE_NAME]
        movement_handler(destination)

def movement_handler(destination):
    print("\n" + "You have moved to " + zonemap[myPlayer.location][ZONE_NAME] + ". " + zonemap[myPlayer.location][DESCRIPTION])
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already discovered everything here.")
    else:
        print(zonemap[myPlayer.location][EXAMINATION])
  

######################################################################## Game functionality ####################################################################
def start_game():
    setup_game()

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # Handle if puzzles are solved etc...

def setup_game():
    os.system('cls')

    # NAME COLLECTION
    question1 = "What is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    # CLASS COLLECTION
    question2 = "What is your class?\n"
    question2added = "You can play as a warrior, mage or cleric.\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'cleric']
    if player_job.lower() == 'warrior':
        playsound("music/sword-unsheathe.wav")
    if player_job.lower() == 'mage':
        playsound("music/magic1.wav")
    if player_job.lower() == 'cleric':
        playsound("music/spell.wav")


    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a" + " " + player_job + "\n")

    while player_job.lower() not in valid_jobs:
        player_job = input('> ')
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a" + " " + player_job + ". \n")

    # PLAYER STATS
    myPlayer.hp = 25
    myPlayer.mp = 15


    # INTRODUCTION
    question3 = "Ah yes... " + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

    thee_dots = ". . . . . \n"
    speech1 = "Well met..." + player_name + " and welcome to Galarian. A land of adventue, riches, reknown... BIST. \n" 
    speech2 = "I hope your journey here was pleasant and that the very least, these lands have greeted you well.  \n"
    speech3 = "Just beware of the bisted woodlands. \n"

    for character in thee_dots:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    os.system('cls')

    print("####################")
    print(" --- LETS BEGIN ---")
    print("####################")
    playsound("music/witch.wav")
    main_game_loop()

### MAP ###
"""
a1 a2... Player starts at b2
----
|||| b1
----
|||| b2...
----
||||
----
||||
----
"""
ZONE_NAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east",
SOUND_EFFECT = "sound effect"

solved_places = {
    "a1": False, "a2": False, "a3": False, "a4": False,
    "b1": False, "b2": False, "b3": False, "b4": False,
    "c1": False, "c2": False, "c3": False, "c4": False,
    "d1": False, "d2": False, "d3": False, "d4": False
    }

zonemap = {
    "a1": {
        ZONE_NAME: "Highbury",
        DESCRIPTION: "Highbury is a small town on the outskirts of the 5 kings mountain range.",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "d1",
        DOWN: "b1",
        LEFT: "a4",
        RIGHT: "a2",
        SOUND_EFFECT: "music/spell.wav"
    },
        "a2": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "d2",
        DOWN: "b2",
        LEFT: "a1",
        RIGHT: "a3",
        SOUND_EFFECT: "music/spell.wav"
    },
        "a3": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "d3",
        DOWN: "b3",
        LEFT: "a2",
        RIGHT: "a4"
    },
        "a4": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "A crappy little town",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "d4",
        DOWN: "b4",
        LEFT: "a3",
        RIGHT: "a1"
    },
        "b1": {
        ZONE_NAME: "Town One",
        DESCRIPTION: "The humble town of Highbury.",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "a1",
        DOWN: "c1",
        LEFT: "b4",
        RIGHT: "b2"
    },
        "b2": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "a2",
        DOWN: "c2",
        LEFT: "b1",
        RIGHT: "b3"
    },
        "b3": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "a3",
        DOWN: "c3",
        LEFT: "b2",
        RIGHT: "b4"
    },
        "b4": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "A crappy little town",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "a4",
        DOWN: "c4",
        LEFT: "b3",
        RIGHT: "b1"
    },
        "c1": {
        ZONE_NAME: "Town One",
        DESCRIPTION: "The humble town of Highbury.",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "b1",
        DOWN: "d1",
        LEFT: "c4",
        RIGHT: "c2"
    },
        "c2": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "b2",
        DOWN: "d2",
        LEFT: "c1",
        RIGHT: "c3"
    },
        "c3": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "b3",
        DOWN: "d3",
        LEFT: "c2",
        RIGHT: "c4"
    },
        "c4": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "A crappy little town",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "b4",
        DOWN: "d4",
        LEFT: "c3",
        RIGHT: "c1"
    },
        "d1": {
        ZONE_NAME: "Town One",
        DESCRIPTION: "The humble town of Highbury.",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "c1",
        DOWN: "a1",
        LEFT: "d4",
        RIGHT: "d2"
    },
        "d2": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "c2",
        DOWN: "a2",
        LEFT: "d1",
        RIGHT: "d3"
    },
        "d3": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "description",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "c3",
        DOWN: "a3",
        LEFT: "d2",
        RIGHT: "d4"
    },
        "d4": {
        ZONE_NAME: "Town Two",
        DESCRIPTION: "A crappy little town",
        EXAMINATION: "examine",
        SOLVED: False,
        UP: "d3",
        DOWN: "a4",
        LEFT: "d3",
        RIGHT: "d1"
    },
}


    




title_screen()