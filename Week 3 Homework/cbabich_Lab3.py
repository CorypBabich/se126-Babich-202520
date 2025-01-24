#Cory Babich
#W3D2 Lab3 1D & Parallel Lists
#SE126.06
#1-23-2025 [W1D2]

#VARIABLE DICTIONARY

#file       Holdes the read csv file as a 2D list
#rec        Holds a record from file as a list, for each loop of the for loop
#tooYoung   Holds the number of individuals that are too young to register
#notReg     Holds the number of individuals that can register but have not
#noVote     Holds the number of individuals that registered but didn't vote
#didVote    Holds the number of individuals that voted. 

#--------IMPORTS----------------------------------------------
import csv

#--------FUNCTIONS--------------------------------------------

#--------MAIN EXECUTING CODE----------------------------------

with open("voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)

    tooYoung = 0
    notReg = 0
    noVote = 0
    didVote = 0
    
    for rec in file:

        if( int(rec[1]) < 18 ):
            tooYoung += 1
        elif(rec[2].upper() == 'N'):
            notReg += 1
        elif(rec[3].upper() == 'N'):
            noVote += 1
        else:
            didVote += 1

print(f"\nIndividuals not eligible to register:{tooYoung:2}")
print(f"Individuals who did not Register:{notReg:2}")
print(f"Didn't Vote:{noVote:2}")
print(f"Did Vote:{didVote:2}")



