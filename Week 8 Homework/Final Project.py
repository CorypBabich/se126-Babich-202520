
#Cory Babich
#Lab 6
#SE126.06
#2-18-2025 [W7D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------


#--MAIN EXECUTING CODE----------------------------------

# Player stats and enemy in focus
playerShip = {
    "Name":"SS No Name",
    "HP":10,
    "Atc":5,
    "Def":5
}
currentFoe = {} # This is blank on compliation so that the enemy templates can fill it when they join the fight
                # Funcations and other processes will only referrence the states of currentFoe

# Enemy ship templates
sloop = {
    "name":"Sloop",
    "HP":10,
    "atc":2,
    "def":0
}
battleShip = {
    "name":"Battleship",
    "HP":30,
    "atc":10,
    "def":2
}
capitalShip = {
    "name":"Capitalship",
    "HP":50,
    "atc":20,
    "def":4
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
    print(f"Enemy Ship: {currentFoe["name"]} | HitPoints :{currentFoe["HP"]:2} , Attack :{currentFoe["atc"]:2} , Defence :{currentFoe["def"]:2}")
    
    print(f"\n\nYour Ship: {currentFoe["name"]} | HitPoints :{currentFoe["HP"]:2} , Attack :{currentFoe["atc"]:2} , Defence :{currentFoe["def"]:2}")
    print(f"-\nAttack). ")
    input()

