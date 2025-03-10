
#Cory Babich
#Lab 6
#SE126.06
#2-18-2025 [W7D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv
import random

#--FUNCTIONS-------------------------------------
def enAttack(): 
    return attack(currentFoe, player)
def enDefend():
    return defend(currentFoe)

def attack(attacker, target):
    defence = 1
    if target["isDef"] == True:
        defence = 2
    damage = (attacker["atc"] - target["def"])/defence
    
    # If the target's armor reduces the incoming damage to a negative number, it is set to 0.
    if damage < 0:
        damage = 0

    #Print flavor text for notifying the player, change based on if the player is the attack is or not.
    if attacker == player:
        print(f"Hit them with the Ion Cannons. (You deal {damage} damage)")
    else:
        print(f"Their launching missils! (You take {damage} damage)")

    target["HP"] -= damage

def defend(defender):
    #Sets the calling ship (player or enemy) to is defending. This halves incoming damage in the attack function.
    defender["isDef"] = True  

    if defender == player:
        print("Take evasive maneuvers!")
    else:
        print("Sir! They're dodging our attacks.")


#--MAIN EXECUTING CODE----------------------------------

# Player stats and enemy in focus
player = {
    "name":"SS No Name",
    "HP":10,
    "atc":5,
    "def":5,
    "isDef":False
}
currentFoe = {} # This is blank on compliation so that the enemy templates can fill it when they join the fight
                # Funcations and other processes will only referrence the states of currentFoe

# Enemy ship templates
sloop = {
    "name":"Sloop",
    "HP":10,
    "atc":2,
    "def":0,
    "isDef":False,
    "ability":[enAttack,enDefend]
}
battleShip = {
    "name":"Battleship",
    "HP":30,
    "atc":10,
    "def":2,
    "isDef":False,
    "ability":[enAttack,enDefend]
}
capitalShip = {
    "name":"Capitalship",
    "HP":50,
    "atc":20,
    "def":4,
    "isDef":False,
    "ability":[enAttack,enDefend]
}

# The order in which enemies attack the player
battleOrder = [
    sloop, sloop,
    sloop, battleShip,
    battleShip, capitalShip
]

contineuY = "Y"

currentFoe = sloop
while contineuY == "Y":
    userInput = ""
    player["isDef"] = False

    print("\n")
    print(f"Enemy Ship: {currentFoe["name"]} | HitPoints :{currentFoe["HP"]:2} , Attack :{currentFoe["atc"]:2} , Defence :{currentFoe["def"]:2}")
    print(f"\nYour Ship: {player["name"]} | HitPoints :{player["HP"]:2} , Attack :{player["atc"]:2} , Defence :{player["def"]:2}")
    print(f"-\nYour actions) [Attack]  [Defend]  ")
    userInput = input("-:")

    if userInput.upper() in "ATTACK":
        attack(player, currentFoe)

    elif userInput.upper() in "DEFENCE":
        player["isDef"] = True

    currentFoe["ability"][random.randrange(len(currentFoe["ability"]))]()

