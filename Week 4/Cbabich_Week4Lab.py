#Cory Babich
#W4D1 
#SE126.06
#1-27-2025 [W4D1]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"

    return let

#--Main Executing Code---------------------------

firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

numAverage = []
letAvg = []

with open("Week 4/class_grades-1.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))


for i in range(0, len(firstName)):
    
    #Calculating the averages
    numAverage.append((test1[i] + test2[i] + test3[i])/3)

    #
    letAvg.append(letter(numAverage[i]))
                         
#process the list to display all student data back to the user
print(f"\n{'FNAME':10} {'LNAME':10} {'T1':3} {'T2':3} {'T3':3} {'# AVG':6} {'L AVG'}")
print("--------------------------------------------------------------------------------------------")
for i in range(0, len(firstName)):                
    print(f"{firstName[i]:10} {lastName[i]:10} {test1[i]:3} {test2[i]:3} {test3[i]:3} {numAverage[i]:6.2f}   {letAvg[i]}")
print("--------------------------------------------------------------------------------------------")

print(f"There are {len(firstName)} students in the file.\n")

print("\n\nWelcome to the student finder program\n\n")

answer = input("Would you like to find a student? [y/n]")

while answer == "y":
    print("\n\tSERACH Menu Options")
    print("1. Search by LAST name")
    print("2. Search by LETTER GRADE")
    print("3. EXIT")

    search_type = input("\nEnter prefered option [1-3]: ")

    if search_type == "1":
        found = -1

        search_name = input("\nPlease enter the last name of the student you wish to find.")
        for i in range(0, len(lastName)):
            if search_name.lower() == lastName[i].lower():
                found = i 
        
        if found != -1:
            print(f"\nYou're search for {search_name} was found.")
            print(f"{firstName[found]:10} {lastName[found]:10} {test1[found]:3} {test2[found]:3} {test3[found]:3} {numAverage[found]:6.2f}   {letAvg[found]}")
        else: 
            print(f"This student '{search_name}' is not on the record provided.")

    elif search_type == "2":
        found = []

        search_grade = input("\nPlease enter the last name of the student you wish to find.")
        for i in range(0, len(letAvg)):
            if search_grade.upper() == letAvg[i].upper():
                found.append(i)
        
        if not found: #if the list if empty
            print(f"Letter grades '{search_name}' are not on the record provided.")
        else:
            for i in range(0, len(found)):
                #print(f"\nYou're search for {search_grade}.upper() was found.")
                print(f"{firstName[found[i]]:10} {lastName[found[i]]:10} {test1[found[i]]:3} {test2[found[i]]:3} {test3[found[i]]:3} {numAverage[found[i]]:6.2f}   {letAvg[found[i]]}") 
            

    elif search_type == "3":
        answer = "n"

    else:
        print("\nINVALID INPUT\n")

    if search_type == 1 or search_type == 2:
        answer = input("Would you like to find a student? [y/n]")



