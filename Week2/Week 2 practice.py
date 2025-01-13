

import csv


total_records = 0 #The total number of rows in the CSV file


print(f"{'NAME':10} \t {'NUM':3} \t {'COLOR'}")
print("-----------------------------------------------")
#opens simple.csv and dumps its data into csvfile as a list
with open("Week2/simple.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    #loop through every record(row) in the file
    for record in file:
        total_records += 1

        #print(record)

        name = record[0]
        number = record[1]
        color = record[2]

        print(f"{name:10} \t {number:3} \t {color}")

print("-----------------------------------------------")

print(f"\nTOTAL RECORDS: {total_records}\n")







