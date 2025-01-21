#W2D2 - Text File Handling Review w/ Filters

#PROGRAM PROMPT:

#VARIABLE DICTIONARY:

#roomsTotal     The total number of rows in the CSV file
#roomsOver      The number of rooms over capacity
#name           holds the first field of each record
#roomMax        holds the second field of each record as an INT
#peopleCount    holds the third field of each record as an INT
#over           holds the different between roomMax and peopleCount


#--Imports-------------------------------------------------------------

import csv

#--FUNCTIONS-------------------------------------------------------------

def difference(max, people):
    return (max-people)

#--MAIN EXECUTING CODe-------------------------------------------------------------

roomsTotal = 0 #The total number of rows in the CSV file
roomsOver = 0 #The number of rooms over capacity

print(f"\n{"Name":20} {"Max":5}  {"Min":5}  {"Over"}")
#opens simple.csv and dumps its data into csvfile as a list
with open("Week2/classLab2.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    #loop through every record(row) in the file
    for record in file:
        roomsTotal += 1

        name = record[0]
        roomMax = int(record[1])
        peopleCount = int(record[2])
        over = difference(roomMax,peopleCount)


        if(over < 0):
            roomsOver += 1
            print(f"{name:20} {str(roomMax):5}  {str(peopleCount):5}  {over*-1:4}")


print(f"\nProcessed {roomsTotal} records")
print(f"There are {roomsOver} rooms over the limit.\n")
print("Press any key to continue...\n")









