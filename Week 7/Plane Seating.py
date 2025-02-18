#Cory Babich
#W7D2 
#SE126.06
#2-18-2025 [W4D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------

#--------MAIN EXECUTING CODE----------------------------------

rowMax = 8
seats = []

record = 0
field = 0

for i in range(0, rowMax):
    row = ["A","B","C","D"]
    seats.append(row)

print("\nPlanes seats")
print("-----------------------------")
print("Row:")
for i in range(0, rowMax):
    print(f"{i:3}:  {seats[i][0]} {seats[i][1]}   {seats[i][2]} {seats[i][3]}")

record = input(f"Which row would like to sit in [1 to {rowMax}]: ")
if record > 0 and record <= rowMax:
    print()
else:
    print()

field = input("Which seat do you like to reserve: ")



