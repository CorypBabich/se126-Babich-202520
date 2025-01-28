#Cory Babich
#W4D2 
#SE126.06
#1-28-2025 [W4D2]

#VARIABLE DICTIONARY

# fName  -----  Holds the first name of every employee as a list
# lName         Holds the last name of every employee as a list
# age  -------  Holds the age of every employee as a list
# screenName    Holds the screen name of every employee as a list
# house  -----  Holds the house name of every emplouee as a list
# emails        Holds the email of every employee as a list
# deps  ------  Holds every employee's department as a list
# exts          Holds every employee's extension as a list

# file      Holds the contents of the file as a 2D list
# rec       Holds each record of file as lists

#totRnD  -----  Intcrements for each employee in Research & Development
#totMark        Intcrements for each employee in Marketing
#totHumRes  --  Intcrements for each employee in Human Resources
#totAccounting  Intcrements for each employee in Accounting
#totSales  ---  Intcrements for each employee in Sales
#totAuditing    Intcrements for each employee in Auditing

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------



#--Main Code--------------------------------------

#lists to hold read data from file
fName = []
lName = []
age = []
screenName = []
house = []
emails = []
deps = []
exts = []


totRnD = 0
totMark = 0
totHumRes = 0
totAccounting = 0
totSales = 0
totAuditing = 0

#lists of data to add




with open("got_emails.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        screenName.append(rec[3])
        emails.append(rec[3]+"@westeros.net")
        house.append(rec[4])
        if rec[4] == "House Stark":
            deps.append("Research & Development")
            exts.append("100 - 199")
            totRnD += 1
        elif rec[4] == "House Targaryen":
            deps.append("Marketing")
            exts.append("200 - 299")
            totMark += 1
        elif rec[4] == "House Tully":
            deps.append("Human Resources")
            exts.append("300 - 399")
            totHumRes += 1
        elif rec[4] == "House Lannister":
            deps.append("Accounting")
            exts.append("400 - 499")
            totAccounting += 1
        elif rec[4] == "House Baratheon":
            deps.append("Sales")
            exts.append("500 - 599")
            totSales += 1
        elif rec[4] == "The Night's Watch":
            deps.append("Auditing")
            exts.append("600 - 699")
            totAuditing += 1
        else:
            print("INVALID INPUT")
         

print(f"\n{"First Name":10}  {"Last Name":10} {"emails":28}  {"Department":22}  {"Extensions"}\n-----")

for i in range(0, len(fName)):
    print(f"{fName[i]:10}  {lName[i]:10} {emails[i]:28}  {deps[i]:22}  {exts[i]}")
print("")# Print ending new line for readability

file = open('westeros.csv','w')
file.write(f"{"First Name":10}  {"Last Name":10} {"Emails":28}  {"Department":22}  {"Extensions"}\n-----\n")
for i in range(0, len(fName)):
    if i != (len(fName)-1):
        file.write(f"{fName[i]:10}  {lName[i]:10} {emails[i]:28}  {deps[i]:22}  {exts[i]}\n")
    else:
        file.write(f"{fName[i]:10}  {lName[i]:10} {emails[i]:28}  {deps[i]:22}  {exts[i]}")
file.close()

print(f"\nTotal Employees : {len(fName):5}")
print(f"There are {totRnD:2} Empoyees in Research & Development")
print(f"There are {totMark:2} Empoyees in Marketing")
print(f"There are {totHumRes:2} Empoyees in Human Resources")
print(f"There are {totAccounting:2} Empoyees in")
print(f"There are {totSales:2} Empoyees in Accounting")
print(f"There are {totAuditing:2} Empoyees in Auditing")

print("\n Have a good day.")

