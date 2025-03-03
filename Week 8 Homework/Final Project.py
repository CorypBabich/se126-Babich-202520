
#Cory Babich
#Lab 6
#SE126.06
#2-18-2025 [W7D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv
import random

#--FUNCTIONS-------------------------------------
def updateEnemy(newEnem): #updates current foe states to match the stats of the enemy template it is passed to it.
    currentFoe["name"] = newEnem["name"]
    currentFoe["HP"] = newEnem["HP"]
    currentFoe["atc"] = newEnem["atc"]
    currentFoe["def"] = newEnem["def"]
    currentFoe["ability"] = newEnem["ability"]

def enAttack(): 
    return attack(currentFoe, player)
def enDefend():
    return defend(currentFoe)

def attack(attacker, target):
    damage = (attacker["atc"] - target["def"])

    if target["isDef"] == True:
        damage = damage/2
    
    
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
    defender["isDef"] = True

    if defender == player:
        print(f"Take evasive maneuvers!")
    else:
        print(f"They're trying to dodge our cannons")

#--MAIN EXECUTING CODE----------------------------------

# Player stats and enemy in focus
player = {
    "name":"SS No Name",
    "HPmax":10,
    "HP":10,
    "atc":5,
    "def":5,
    "isDef":False
}
currentFoe = {
    "name":"NoFoeShipError",
    "HP":0,
    "atc":0,
    "def":0,
    "isDef":False,
    "ability":[]
} # This is blank on compliation so that the enemy templates can fill it when they join the fight
                # Funcations and other processes will only referrence the states of currentFoe

# Enemy ship templates
sloop = {
    "name":"Sloop",
    "HP":10,
    "atc":2,
    "def":0,
    "ability":[enAttack,enDefend]
}
battleShip = {
    "name":"Battleship",
    "HP":30,
    "atc":10,
    "def":2,
    "ability":[enAttack,enDefend]
}
capitalShip = {
    "name":"Capitalship",
    "HP":50,
    "atc":20,
    "def":4,
    "ability":[enAttack,enDefend]
}

# The order in which enemies attack the player
battleOrder = [
    sloop, sloop,
    sloop, battleShip,
    battleShip, capitalShip
]

contineuY = "Y"
battleNum = 0

updateEnemy(battleOrder[battleNum]) #Sets the stats of currentFoe to the stats of the first enemy in the battle order list
while contineuY == "Y":
    userInput = ""
    player["isDef"] = False #if the player defended last turn, it is reset at the start of this turn

    print("\n")
    print(f"Enemy Ship: {currentFoe["name"]} | HitPoints :{currentFoe["HP"]:2} , Attack :{currentFoe["atc"]:2} , Defence :{currentFoe["def"]:2}")
    print(f"\nYour Ship: {player["name"]} | HitPoints :{player["HP"]:2} , Attack :{player["atc"]:2} , Defence :{player["def"]:2}")
    print(f"-\nYour actions) [Attack]  [Defend]  ")
    userInput = input("-:")

    if userInput.upper() in "ATTACK":
        attack(player, currentFoe)

    elif userInput.upper() in "DEFENCE":
        player["isDef"] = True

    currentFoe["isDef"] = False #if the enemy defended last turn, it is reset after the player's action but before it takes a turn.
    
    currentFoe["ability"][random.randrange(len(currentFoe["ability"]))]()
    '''
                                                                       () "The rest of the line determines the function location, these parentheses"
    currentfoe["ability"]                                                 "references the ability list, in the currentfoe dictionary"
                         [                                            ]   "indicates the position of the ability list needed."
                          random.randrange(                          )    "Returns a random number from 0 to the number given"
                                           len(currentFoe["ability"])     "returns the length of the ability list"
    '''

    if currentFoe["HP"] <= 0:
        print("\n!!! Ship Destroyed Captain !!!")
        print("But a new enemy approaches")
        input("\n(Press any button to continue)")

        #Heal the player to full health
        player["HP"] = player["HPmax"]

        #increase the fight indicator by one and redefine the currentFoe accordingly
        battleNum += 1
        updateEnemy(battleOrder[battleNum])



