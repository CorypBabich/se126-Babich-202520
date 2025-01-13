

import csv

with open("Week 2 Homework/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:

        print(record)

        if(record[0].upper() == "D"):
            Type = "Desktop"
        elif(record[0].upper() == "L"):
            Type = "Laptop"
        else:
            print(f"***ERROR UNEXPECTED DATA TYPE*** ({record[0]})")

        brand = record[1]
        cpu = record[2]

        print(f"{Type:5} \t {brand:5} \t {cpu:5} \t {ram:5} \t {disk1st:5} \t {numHDD:5}")

print("-----------------------------------------------")

















