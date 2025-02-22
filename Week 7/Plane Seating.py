#Cory Babich
#W7D2 
#SE126.06
#2-18-2025 [W4D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------

def showSeats():
    print("\nPlanes seats")
    print("-----------------------------")
    print("Row:")
    for i in range(0, rowMax):
        print(f"{i+1:3}:  {seats[i][0]} {seats[i][1]}   {seats[i][2]} {seats[i][3]}")
    print("")# Newline for readability  

#--MAIN EXECUTING CODE----------------------------------

continueY = "Y"
rowMax = 8
seats = []

record = 0
field = 0

for i in range(0, rowMax):
    row = ["A","B","C","D"]
    seats.append(row)

showSeats()
while continueY.upper() == "Y":

    record = input(f"Which row would like to sit in [1 to {rowMax}]: ")
    while int(record) < 1 or int(record) > rowMax:
        print("***INVALID INPUT***")
        record = input(f"{record} is not a valid input. Please enter value from [1 to {rowMax}]:")

    field = input("Which seat do you like to reserve [A, B, C, or D]: ")
    while field.upper() != "A" and field.upper() != "B" and field.upper() != "C" and field.upper() != "D":
        print("***INVALID INPUT***")
        field = input(f"{field} is not a valid input. Please enter value of [A, B, C, or D]:")

    if field.upper() == "A":
        field = 0
    elif field.upper() == "B":
        field = 1
    elif field.upper() == "C": 
        field = 2
    else:
        field = 3

    if seats[(int(record)-1)][field] == "x":
        print(f"Seat {record}{field}This seat has already been booked.\n")
    else:
        seats[(int(record)-1)][field] = "x"

    showSeats()

    continueY = input("Do you want to book another seat [Y/N] :")
    while continueY.upper() != "Y" and continueY.upper() != "N":
        print("***INVALID INPUT***")
        field = input(f"{continueY} is not a valid input. Please enter the character Y or N :")

print("Goodbye, Have a good day!")
