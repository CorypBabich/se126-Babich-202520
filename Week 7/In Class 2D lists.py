#Cory Babich
#W7D2 
#SE126.06
#2-18-2025 [W4D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------

def menu():
    print("Simple Search Menu")
    print("1. Search by Name")
    print("2. Search by Numer")
    print("3. Search by Color")
    print("4. EXIT")

    return input("Enter your search choice [1-4]: ")

def swap(k, list):
    holder = list[k]
    list[k] = list[k + 1]
    list[k + 1] = holder

#--------MAIN EXECUTING CODE----------------------------------

names = [] 
nums = []
colors = []

valid_menu = ["1","2","3","4"]

with open("Week 7/simple-2.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        names.append(rec[0])
        nums.append(rec[1])
        colors.append(rec[2])

ans = "y"

while ans == "y":
    choice = menu()

    if choice not in valid_menu:
        print("***INVALID ENTRY***")
    elif choice == '1':
        print("\nSearch by NAME")

        for i in range(len(names) - 1):
            for k in range(len(names) - 1):
                if names[k] > names[k + 1]:
                   swap(k, colors)
                   swap(k, names)
                   swap(k, nums)

        min = 0
        max = len(names) - 1
        mid = int((min+max) / 2)

        search = input("enter the NAME you are looking for: ")
        
        while min < max and search.lower() != names[mid].lower():
            if search.lower() < names[mid].lower():
                max = mid - 1
            else:
                min = mid + 1 
            mid = int((min+max) / 2)   

        if search.lower() == names[mid].lower():
            print(f"The search for {search} is complete!")
            print(f"{'NAME':8}    {'NUM':3}     {'COLOR'}")
            print("-------------------------------------------")
            print(f"{names[mid]:8}    {nums[mid]:3}     {colors[mid]}")
            print("-------------------------------------------")
        else:
            print(f"Your Search for {search} is complete, and no information was found: ")

    elif choice == '2':
        print("\nSearch by NUM")



    elif choice == '3':
        print("\nSearch by COLOR")
        
        for i in range(len(colors) - 1):
            for k in range(len(colors) - 1):
                if colors[k] > colors[k + 1]:
                   swap(k, colors)
                   swap(k, names)
                   swap(k, nums) 
        
        min = 0
        max = len(names) - 1
        mid = int((min+max) / 2)

        search = input("enter the NAME you are looking for: ")
        
        while min < max and search.lower() != names[mid].lower():
            if search.lower() < names[mid].lower():
                max = mid - 1
            else:
                min = mid + 1 
            mid = int((min+max) / 2)   

        if search.lower() == names[mid].lower():
            print(f"The search for {search} is complete!")
            print(f"{'NAME':8}    {'NUM':3}     {'COLOR'}")
            print("-------------------------------------------")
            print(f"{names[mid]:8}    {nums[mid]:3}     {colors[mid]}")
            print("-------------------------------------------")
        else:
            print(f"Your Search for {search} is complete, and no information was found: ")

    else:
        print("\nEXIT")
        ans = "n"

print("Goodbye, and have a good day.")


#--------DataFile----------------------------------

dataFile = [names,nums,colors]

print("\n\nData File (2D List[][]):")
for i in range(0, len(dataFile)):
    print(f"INDEX {i} of 'DataFile': {dataFile[i]}")

    for k in range(0, len(dataFile[i])):
        print(f"INDEX {i} and value DataFile[{k}]: {dataFile[i][k]}")

