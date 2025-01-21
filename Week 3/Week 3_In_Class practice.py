#Cory Babich
#W3D2 - List Review - 1Dimensional Lists & Parallel Lists
#SE126.06
#1-21-2025 [W3D2]

#This File uses: class_grades.csv 

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------


#--Main Executing Code---------------------------

total_records = 0

#create a list for every potential field
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

with open("Week 3/class_grades.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    for rec in file:
        

        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#Disconmect from file

#holds all students' test score average
avg = []

for i in range(0, len(test1)):
    avg.append((test1[i]+test2[i]+test3[i])/3)


print(f"\nINDEX {' #'} : {'First':10} {'Last':10} {'T1':3} {' T2'} {' T3'}  {'AVG':3}")
print("------------------------------------------------------------------------")
#basic processing - use the 1D parallal lists to print all data to the console

for index in range(0,len(firstName)):
    print(f"INDEX {index:2} : {firstName[index]:10} {lastName[index]:10} {test1[index]:3} {test2[index]:3} {test3[index]:3}  {avg[index]:5.2f}")        
print("------------------------------------------------------------------------")

#currect Class Average
total_avg = 0

for i in range(0, len(avg)):
    total_avg += avg[i]

total_avg = total_avg / len(avg)
print(f"\nThe CLASS AVERAGE of these {len(avg)} students is: {total_avg:.2f}\n")


