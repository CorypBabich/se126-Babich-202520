#YOUR NAME
#W1D2 Lab Demo: SE116 Review
#SE126.06
#1-7-2025 [W1D2]

#PROGRAM PROMPT: This is a temperature conversion program, it allows a user to enter as many Fahrenheit temps as they'd like and then shows the Celsius conversoion for each. It also counts the number of temps and determines the average of all temps entered. 

#VARIABLE DICTIONARY


#--------IMPORTS----------------------------------------------

#--------FUNCTIONS--------------------------------------------

def difference(people, max_cap):
    dif = max_cap - people
    return dif

#This function is called when user is promted for a yes or no to continue the program, a loop repates the input prompt until the user provide the expect input
def userTrap():
    answer = input("Is there another room you'd like to compare against fire safety compliance [n/y] :").lower()
    while(answer != 'y' and answer != 'n'):
        print("***Invalid Input*** \n Please enter the character 'y' for YES or the character 'n' for NO")
        answer = input("Is there another room you'd like to compare against fire safety compliance [n/y] :").lower()

    return answer

#--------MAIN EXECUTING CODE----------------------------------

#initializing needed variables

roomMax = 0
peopleCount = 0
continueY = "y"
inRoom = 0 #holds the diffence between room capacity and number of people

while continueY == "y":
    roomMax = int(input("How many people can the room hold: "))
    peopleCount = int(input("How many people will be in the room: "))
    
    inRoom = difference(peopleCount, roomMax)

    if(inRoom > 0):
        print(f"This room is fire safety compliant! It can fit an additional {inRoom} people and remain compliant.")
    elif(inRoom == 0):
        print("This room meets fire safety requirements, but cannot accommodate without breaking fire safety regulations.")
    else:
        print(f"This room is NOT fire safety compliant! This room is over capacity by {(inRoom * -1)} people.")

    continueY = userTrap()

