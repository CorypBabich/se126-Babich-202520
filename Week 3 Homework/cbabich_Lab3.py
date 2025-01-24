#Cory Babich
#W3D2 Lab3 1D & Parallel Lists
#SE126.06
#1-23-2025 [W1D2]

#PROGRAM PROMPT:  

#VARIABLE DICTIONARY



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
        elif(rec[2] == 'N'):
            notReg += 1
        elif(rec[3] == 'N'):
            noVote += 1
        else:
            didVote += 1

print(f"Too Young:{tooYoung:2} Didn't Register:{notReg:2}")
print(f"Didn't Vote:{noVote:2} Did Vote: {didVote:2}")




