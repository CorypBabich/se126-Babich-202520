
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
    currentFoe["HPmax"] = newEnem["HPmax"]
    currentFoe["atc"] = newEnem["atc"]
    currentFoe["def"] = newEnem["def"]
    currentFoe["ability"] = newEnem["ability"]


def enAttack(): 
    return attack(currentFoe, player)
def enEmp():
    return empAttack(currentFoe, player)
def enDefend():
    return defend(currentFoe)
def enRepair():
    return repair(currentFoe)

def attack(attacker, target):
    damage = attacker["atc"]

    #reduce damage if the target is defending
    if target["isDef"] == True:
        damage = damage/2
    
    #increase damage if the attacker is aiming


    damage = damage - target["def"]

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

def repair(repairer):
    repairNum = (1 + random.randrange(5)) + (1 + random.randrange(5)) # Randomly generates 2 random values ranging from 1 to 6 and adds them together
    
    if repairer["HP"] + repairNum > repairer["HPmax"]:
        repairer["HP"] = repairer["HPmax"]
        
        if repairer == player:
            print("We're fully repaired Captain!")
        else:
            print("The enemy fully fixed their ship!")
    else:
        repairer["HP"] += repairNum

        if repairer == player:
            print(f"Repairs underway! (You healed {repairNum} HP)")
        else:
            print(f"They're repairing their Ship! (The enemy healed {repairNum} HP)")

def empAttack(attacker, target):
    damage = int(attacker["atc"] / 2)
    damage = damage - target["def"]
    target["HP"] -= damage
    target["isEMP"] = True



#--MAIN EXECUTING CODE----------------------------------

# Player stats and enemy in focus
player = {
    "name":"SS No Name",
    "HPmax":10,
    "HP":10,
    "atc":5,
    "def":5,
    "isDef":False,
    "isEMP":False
}
currentFoe = {
    "name":"NoFoeShipError",
    "HP":0,
    "HPmax":0,
    "atc":0,
    "def":0,
    "isDef":False,
    "isEMP":False, 
    "ability":[]
} # This is blank on compliation so that the enemy templates can fill it when they join the fight
                # Funcations and other processes will only referrence the states of currentFoe

# Enemy ship templates
sloop = {
    "name":"Sloop",
    "HP":10,
    "HPmax":10,
    "atc":2,
    "def":0,
    "ability":[enAttack,enDefend]
}
battleShip = {
    "name":"Battleship",
    "HP":30,
    "HPmax":30,
    "atc":10,
    "def":2,
    "ability":[enAttack,enDefend,enRepair]
}
capitalShip = {
    "name":"Capitalship",
    "HP":50,
    "HPmax":50,
    "atc":20,
    "def":4,
    "ability":[enAttack,enDefend,enRepair,enEmp]
}

# The order in which enemies attack the player
battleOrder = [
    sloop, battleShip,
    battleShip, capitalShip
]

contineuY = "Y"
battleNum = 0

chargeNum = 100
chargeDisplay = "Ready!"
menuInput = 0
exitGame = 0

print("\nWelcome to Austin and Cory's Ship!")
print("1. Play Game \n2. How to Play \n3. Exit")

while contineuY == "Y":
    menuInput = input("-:")

    #If the player enters 1 at the menu, the game starts.
    if menuInput == "1":

        updateEnemy(battleOrder[battleNum]) #Sets the stats of currentFoe to the stats of the first enemy in the battle order list
        while contineuY == "Y":
            userInput = ""
            player["isDef"] = False #if the player defended last turn, it is reset at the start of this turn

            #The player's EMP blast has to charge for roughly 4 turns, this is handled here by generating a random number from 1 to 15 plus 23
            #The result is added to --
            if chargeNum < 100:
                chargeNum += 23 + ( 1 + random.randrange(14))
                chargeDisplay = str(chargeNum) + "%"
            else:
                chargeDisplay == "Ready!"

            print("\n")
            print(f"Enemy Ship: {currentFoe["name"]:12} | HitPoints :{currentFoe["HP"]:2} , Attack :{currentFoe["atc"]:2} , Defence :{currentFoe["def"]:2}")
            print(f"Your Ship : {player["name"]:12} | HitPoints :{player["HP"]:2} , Attack :{player["atc"]:2} , Defence :{player["def"]:2}")
            print(f"-\nYour actions) [Attack]  [Defend]  [Repair]  [EMP : {chargeDisplay}] {"":65} [Exit: Leave game]")
            #Taking the player's requested action
    

            while userInput.upper() == "": #userInput is blank by defeault, but if the user gives an invalid input it will be set back to "" to 
                                   #repeat the prompt until they do. 
                if player["isEMP"] == False:
                    userInput = input("-:")
                else:
                    # While affected by the EMP, the user's turn is skipped. 
                    # This input is used to comminucate that to the player, but any input they give is ignored.
                    input("-: ()") 
                    #The userInput is set to "**" to break the loop          
                    userInput = "**"

                #Player is attacking  
                if userInput.upper() in "ATTACK":
                    attack(player, currentFoe)# the attack function is called, and is passed he player 

                #Player is defending
                elif userInput.upper() in "DEFENCE":
                    player["isDef"] = True

                #Player repairs their ship to regains hit points.
                elif userInput.upper() in "REPAIR":
                    repair(player)

                elif userInput.upper() in "EMP":
                    if chargeNum >= 100:
                        empAttack(player, currentFoe)
                        print("Player uses EMP Blast")
                        chargeNum = 0
                    else:
                        print("Captain, the EMP is still charging. Try Something Else.")
                        userInput = ""
                elif userInput.upper() in "EXIT":
                    print("is exit")
                    contineuY = "N"
                    ##userInput = "**"

                else:
                    print("*** Invalid Input")
                    userInput = ""

            player["isEMP"] = False # If the player was hit by an EMP last turn, the EMP Status ends here.
            currentFoe["isDef"] = False #if the enemy defended last turn, it is reset after the player's action but before it takes a turn.
    
            if currentFoe["isEMP"] == False: #if the enemy is not under the effects of an EMP they take their turn.
                currentFoe["ability"][random.randrange(len(currentFoe["ability"]))]() #This is the weirdedest line of code I've ever written so below it is a break down. 
                '''
                                                                                   () "The rest of the line determines the function location, these parentheses"
                currentfoe["ability"]                                                 "references the ability list, in the currentfoe dictionary"
                                     [                                            ]   "indicates the position of the ability list needed."
                                      random.randrange(                          )    "Returns a random number from 0 to the number given"
                                                       len(currentFoe["ability"])     "returns the length of the ability list"
                '''
            else:
                currentFoe["isEMP"] = False
                print("They're stunned by the EMP, Sir!")

            if currentFoe["HP"] <= 0:
                print("\n!!! Ship Destroyed Captain !!!")
                print("But a new enemy approaches")
                input("\n(Press any button to continue)")

                #Heal the player to full health
                player["HP"] = player["HPmax"]

                #increase the fight indicator by one and redefine the currentFoe accordingly
                battleNum += 1
                updateEnemy(battleOrder[battleNum])

    elif menuInput == "2":
        print("\nThis game plays as a turn based combat, each turn the player enters in one of the following commands:")
        print("[Attack]")
        print("[Defence]")
        print("[Repair] : Regain hit points &&&&(2d6)")
        print("[EMP] : The enemy's net turn is skipped")

    elif menuInput == "3": #Player leaves the game, set ContineuY to any value that is not "Y" to end the loop.
        contineuY = "N"
    else: 
        print("**INVALID INPUT**")
        print(f"{menuInput} is not a valid choice. Please enter an input of [1,2, or 3]")
   
print("\nGoodbey, and have a good day.\n")
