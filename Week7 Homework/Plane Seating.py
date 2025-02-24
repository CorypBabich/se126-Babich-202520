#Cory Babich
#Lab 6
#SE126.06
#2-18-2025 [W7D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------

def showSeats(): #Print the seating chart
    print("\nPlanes seats")
    print("-----------------------------")
    print("Row:")
    for i in range(0, rowMax):
        print(f"{i+1:3}:  {seats[i][0]} {seats[i][1]}   {seats[i][2]} {seats[i][3]}")
    print("")# Newline for readability  

def checkCharacters(x):
    if x[0] in "abcdefghijklmnopqrstuvwxyz":
        return True #if the first character of x is in the alphabet then it is not a number, and true is returned to continue the input trap
    else:
        return False

#--MAIN EXECUTING CODE----------------------------------

continueY = "Y"
rowMax = 7
seats = []

record = 0
field = 0
fieldNum = ""

for i in range(0, rowMax):
    row = ["A","B","C","D"]
    seats.append(row)

showSeats()
while continueY.upper() == "Y":

    #Takes the input for which row the user wants, and loops the input trap until the input is 
    #between 0 and the row max, the input is 1 character long, and only contains numbers 
    record = input(f"\nWhich row would like to sit in [1 to {rowMax}]: ")
    while len(record) != 1 or checkCharacters(record) or int(record) < 1 or int(record) > rowMax:
        print("***INVALID INPUT***")
        record = input(f"{record} is not a valid input. Please enter value from [1 to {rowMax}]:")

    #Takes the input for which seat in the row the user wants, and loops the input trap until the input is 
    #equal to either A, B, C, or D
    field = input("\nWhich seat do you like to reserve [A, B, C, or D]: ")
    while field.upper() != "A" and field.upper() != "B" and field.upper() != "C" and field.upper() != "D":
        print("***INVALID INPUT***")
        field = input(f"{field} is not a valid input. Please enter value of [A, B, C, or D]:")

    #Assigns fieldNum an index based on the user's input
    if field.upper() == "A":
        fieldNum = 0
    elif field.upper() == "B":
        fieldNum = 1
    elif field.upper() == "C": 
        fieldNum = 2
    else:
        fieldNum = 3

    #Check to see if seat is already booked. If not book it, if it is inform user. 
    if seats[(int(record)-1)][fieldNum] == "x":
        print(f"\nSeat ({record}{field.upper()}) has already been booked.\n")
    else:
        seats[(int(record)-1)][fieldNum] = "x"

    #Display the chart
    showSeats()

    #Ask the user of they would like to continue, Looping the input trap until the input is either 
    continueY = input("Do you want to book another seat [Y/N] :")
    while continueY.upper() != "Y" and continueY.upper() != "N":
        print("***INVALID INPUT***")
        continueY = input(f"{continueY} is not a valid input. Please enter the character Y or N :")

print("\nGoodbye, Have a good day!\n")
