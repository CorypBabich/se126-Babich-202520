#Cory Babich
#W2D2 Lab2 Individual.py
#SE126.06
#1-7-2025 [W1D2]

#PROGRAM PROMPT: This is a temperature conversion program, it allows a user to enter as many Fahrenheit temps as they'd like and then shows the Celsius conversoion for each. It also counts the number of temps and determines the average of all temps entered. 

#VARIABLE DICTIONARY

# file      holds the read csv file
# record    holds the record as indicated by the for loop

# pcType    holds the pc type, recorded from the file record
# pcBrand   holds the pc brand, recorded from the file record
# cpu       holds the CPU info, recorded from the file record
# ram       holds the RAM info, recorded from the file record
# disk1st   holds the 1st Disk info, recorded from the file record
# numHDD    hold the number of HDDs used, recorded from the file record
# disk2nd   holds the 2nd Disk info if pressent, recorded from the file record
# os        holds OS version, recorded from the file record
# year      holds the cp's year, recorded from the file record


#--------IMPORTS----------------------------------------------
import csv

#--------FUNCTIONS--------------------------------------------

#--------MAIN EXECUTING CODE----------------------------------


with open("Week 2 Homework/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    print(f"\n{"Type":7} \t {"Brand":7} \t {"CPU":5} \t {"RAM":5} \t {"1st Disk":7} \t {"NO HDD":7} \t {"2nd Disk":5} \t {"OS":5} \t {"YR":5}")
    print("--------------------------------------------------------------------------------------")

    for record in file:

        #determine the Computer type
        if(record[0].upper() == "D"):
            pcType = "Desktop"
        elif(record[0].upper() == "L"):
            pcType = "Laptop"
        else:
            print(f"***ERROR UNEXPECTED DATA TYPE*** ({record[0]})")

        #determine the brand
        if(record[1] == "DL"):
            pcBrand = "DELL"
        elif(record[1] == "GW"):
            pcBrand = "Gateway"
        else:
            pcBrand = record[1]

        #record cpu, ram, 1st Disk, and HDD number info
        cpu = record[2]
        ram = record[3]
        disk1st = record[4]
        numHDD = record[5]
        
        if(int(numHDD) == 1):
            os = record[6]
            year = record[7]

            print(f"{pcType:7} \t {pcBrand:7} \t {cpu:5} \t {ram:5} \t {disk1st:7} \t {numHDD:20} \t \t {os:5} \t {year:5}")
        else:
            disk2nd = record[6]
            os = record[7]
            year = record[8]

            print(f"{pcType:7} \t {pcBrand:7} \t {cpu:5} \t {ram:5} \t {disk1st:7} \t {numHDD:7} \t {disk2nd:10} \t {os:5} \t {year:5} \n")


















