#Cory Babich
#W4D2 
#SE126.06
#7-3-2025 [W4D2]

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

#rnd_ext  ----  Intcrements for each Research & Development Extention
#mark_ext       Intcrements for each Marketing Extention
#human_ext  --  Intcrements for each Human Resources Extention
#account_ext    Intcrements for each Accounting Extention
#sales_ext  --  Intcrements for each Sales Extention
#audit_ext      Intcrements for each Auditing Extention

#totRnD  -----  Intcrements for each employee in Research & Development
#totMark        Intcrements for each employee in Marketing
#totHumRes  --  Intcrements for each employee in Human Resources
#totAccounting  Intcrements for each employee in Accounting
#totSales  ---  Intcrements for each employee in Sales
#totAuditing    Intcrements for each employee in Auditing



#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------


#lists to hold read data from file
fName = []
lName = []
age = []
screenName = []
house = []
emails = []
deps = []
exts = []

rnd_ext = 0
mark_ext = 0
human_ext = 0
account_ext = 0
sales_ext = 0
audit_ext = 0

totRnD  = 0
totMark = 0
totHumRes = 0
totAccounting = 0
totSales = 0
totAuditing = 0

with open("Week 4 Homework/got_emails.csv") as csvfile:

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
            exts.append(100 + rnd_ext)
            rnd_ext += 1
            totRnD += 1
        elif rec[4] == "House Targaryen":
            deps.append("Marketing")
            exts.append(200 + mark_ext)
            mark_ext += 1
            totMark += 1
        elif rec[4] == "House Tully":
            deps.append("Human Resources")
            exts.append(300 + human_ext)
            human_ext += 1
            totHumRes += 1
        elif rec[4] == "House Lannister":
            deps.append("Accounting")
            exts.append(400 + account_ext)
            account_ext += 1
            totAccounting += 1
        elif rec[4] == "House Baratheon":
            deps.append("Sales")
            exts.append(500 + sales_ext)
            sales_ext += 1
            totSales += 1
        elif rec[4] == "The Night's Watch":
            deps.append("Auditing")
            exts.append(600 + audit_ext)
            audit_ext += 1
            totAuditing += 1
        else:
            print("INVALID INPUT")
        

print(f"\n{"First Name":10}  {"Last Name":10} {"emails":28}  {"Department":22}  {"Extensions"}\n----------------------------------------------------------------------------------")

for i in range(0, len(fName)):
    print(f"{fName[i]:10}  {lName[i]:10} {emails[i]:28}  {deps[i]:22}  {exts[i]}")

print(f"\nThe file is open")
file = open('westeros.csv','w') 
for i in range(0, len(fName)):
    if i != (len(fName)-1):
        file.write(f"{fName[i]},{lName[i]},{emails[i]},{deps[i]},{exts[i]}\n")
    else:
        file.write(f"{fName[i]},{lName[i]},{emails[i]},{deps[i]},{exts[i]}")
file.close()
print(f"The file is closed\n")

print(f"Number of Employees in Research & Development: {totRnD:2}")
print(f"Number of Employees in Marketing: {totMark:2}")
print(f"Number of Employees in Human Resources: {totHumRes:2}")
print(f"Number of Employees in Accounting: {totAccounting:2}")
print(f"Number of Employees in Sales: {totSales:2}")
print(f"Number of Employees in Auditing: {totAuditing:2}")
print("")# Print ending new line for readability




