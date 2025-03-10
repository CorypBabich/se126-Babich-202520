#Cory Babich
#W4D2 
#SE126.06
#1-28-2025 [W4D2]

#VARIABLE DICTIONARY

# fName = []
# lName = []
# age = []
# screenName = []
# house = []
# emails = []
# deps = []
# exts = []

# file
# rec


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
        elif rec[4] == "House Targaryen":
            deps.append("Marketing")
            exts.append(200 + mark_ext)
            mark_ext += 1
        elif rec[4] == "House Tully":
            deps.append("Human Resources")
            exts.append(300 + human_ext)
            human_ext += 1
        elif rec[4] == "House Lannister":
            deps.append("Accounting")
            exts.append(400 + account_ext)
            account_ext += 1
        elif rec[4] == "House Baratheon":
            deps.append("Sales")
            exts.append(500 + sales_ext)
            sales_ext += 1
        elif rec[4] == "The Night's Watch":
            deps.append("Auditing")
            exts.append(600 + audit_ext)
            audit_ext += 1
        else:
            print("INVALID INPUT")
        

print(f"\n{"First Name":10}  {"Last Name":10} {"emails":28}  {"Department":22}  {"Extensions"}\n----------------------------------------------------------------------------------")

for i in range(0, len(fName)):
    print(f"{fName[i]:10}  {lName[i]:10} {emails[i]:28}  {deps[i]:22}  {exts[i]}")
print("")# Print ending new line for readability

file = open('westeros.csv','w') 
for i in range(0, len(fName)):
    if i != (len(fName)-1):
        file.write(f"{fName[i]:10}  {lName[i]:10} {emails[i]:28}  {deps[i]:22}  {exts[i]}\n")
    else:
        file.write(f"{fName[i]:10}  {lName[i]:10} {emails[i]:28}  {deps[i]:22}  {exts[i]}")
file.close()




