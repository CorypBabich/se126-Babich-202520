

import csv


library = {
    "1230" : "Red Rising",
    "1231" : "The little prince"
}

testDiction = {
    "Number": [],
    "Title": []
}

bookNums = []
titles = []


with open("Week 8\dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        bookNums.append(rec[0])
        testDiction["Number"].append(rec[0])
        
        titles.append(rec[1])
        testDiction["Title"].append(rec[1])

        library.update({rec[0]:rec[1]})

print(f"\n{"Num#":6} Title")
print(f"-" * 40)
for key in library:
    print(f"{key:6} {library[key]}")

search = input("\nEnter the TITLE you are looking for: ")
found  = 0

for key in library:
    if search.lower() == library[key].lower():
        #store the found title's location in the dictionary --->
        found = key

if found != 0 : 
    print(f"\nKEY:{found:6}\tTITLE:{library[found]}")
else:
    print(f"\nYour search for {search} came up empty :( ")


id_list = []
index = 0
for key in library:
    id_list.append()



