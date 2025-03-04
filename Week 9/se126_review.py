#W9D2 - SE126 Course Review



#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------
def swap(j,listName):
    temp = listName[j]
    listName[j] = listName[j + 1]
    listName[j + 1] = temp


#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)                            #entire list
print(names_list[0])                         #first value  
print(names_list[len(names_list) - 1])       #last value

#creates an empty field for each potential field
# these MUST remian the same length in order to be parallel
names = []
riders = []
nums = []
color1 = []
color2 = []


#creation & population of dictionaries
people_dictionary ={
    #"key" : value
    "fname" : "George",
    "mname" : "Bulleit",
    "lanme" : "Wayne",
    "age" : 12
}

print(people_dictionary)
print(people_dictionary["fname"])


dragon_dict = {}

#gaining data from a text file 
with open("Week 9/dragons-1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #print() #we will replace this during demo

        #adding data to a list 
        names.append(rec[0])
        riders.append(rec[1])
        nums.append(rec[2])
        color1.append(rec[3])
        if rec[2] == "2":
            color2.append(rec[4])
            color_var = rec[4]
        else:
            color2.append("--")
            color_var = "--"

        #adding data to a dictionary
        dragon_dict.update({rec[0] : [rec[1],rec[2],rec[3], color_var]})


#processing data from collections
print(f"{'NAMES':12} {'RIDERS':30} {'NUM':3} {'COLOR1':8} {'COLOR2'}")
print("-" * 50)
for i in range(0, len(names)):
    print(f"{names[i]:12} {riders[i]:30} {nums[i]:3} {color1[i]:8} {color2[i]}")
print("-" * 50)

for key in dragon_dict:
    print(f"{key.upper()} {dragon_dict[key]}")

    for value in dragon_dict[key]:
        print(f"{key} - {value}", end = "")
    print()
    for i in range(len(dragon_dict[key])):
        print(f"{key} / {dragon_dict[key][i]}", end = "")
    print("\n")
print("-" * 50)


#searching & sorting

search = input("\nEnter the Rider name you wish to find: ")
found = []

for key in dragon_dict:
    if search.lower() in dragon_dict[key][0].lower():
        found.append(key) #adds key of found location to the list

if not found:
    print(f"\nSorry, your search for {search} came up empty :[\n")
else:
    print(f"\n Here are the results {search}: ")
    for i in range(len(found)):
        print(f"{found[i].upper():15} {dragon_dict[found[i]][0]} {dragon_dict[found[i]][1]} {dragon_dict[found[i]][2]} {dragon_dict[found[i]][3]}")



#Bubbl search
for i in range(len(names) - 1):
    for j in range(len(names) - 1):
        if names[j] > names[j + 1]:
            swap(j, names)
            swap(j, riders)
            swap(j, nums)
            swap(j, color1)
            swap(j, color2)

#Binary Search

search = input("\n Which dragon do you want to find: ")

min = 0
max = len(names) - 1
mid = int((min + max)/2)

while min < max and search.lower() != names[mid].lower():
    if search.lower() < names[mid].lower():
        max = mid - 1
    else:
        min = mid + 1
    mid = int((min + max) / 2)
    
print(names[mid].lower())
if search.lower() == names[mid].lower():
    print(f"\nThe Dragon has been found!")
    print(f"\n{names[mid]:12} {riders[mid]:30} {nums[mid]:3} {color1[mid]:8} {color2[mid]} \n")
else:
    print(f"\nSorry m'lord, the dragon remains ellusive.")



#2D lists - lists of lists! 

letters = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]

print(letters)
print(letters[0])
print(letters[0][0])
print(letters[0][len(letters[0]) - 1])

