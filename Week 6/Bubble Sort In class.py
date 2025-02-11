#Cory Babich
#W6D2 
#SE126.06
#2-11-2025 [W4D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------
def display(x, foundList, records):
    '''
    x  =======  is passed the index

    records  =  is the length of the list we are going to process throguh (number of loops/prints)
    '''

    print(f"{'CLASS':8} {'NAMe':10} {'MEANING':20} {'CULTURE'}")

    if x != "x":
        print(f"{class_type[x]:8} {name[x]:10} {meaning[x]:20} {culture[x]}")
    elif foundList: 
        for i in range(0, records):
            print(f"{class_type[foundList[i]]:8} {name[foundList[i]]:10} {meaning[foundList[i]]:20} {culture[foundList[i]]}")
    else:
        for i in range(0, records):
            print(f"{class_type[i]:8} {name[i]:10} {meaning[i]:20} {culture[i]}")

def swap(i,listName):
        temp = listName[i]
        listName[i] = listName[i + 1]
        listName[i + 1] = temp

#--------MAIN EXECUTING CODE----------------------------------


class_type = []
name = []
meaning = []
culture = []

example = ["Tiamat", "Bahamit", "Garax", "Krath"]

with open("Week 6/party.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    for rec in file:
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])


display(9, 0, len(class_type))

ans = input("\nsearch program? You want? [y/n]").lower()

#Answer trap
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [y/n]").lower()

#main loop
while ans == "y":
    print("\n\tSEARCHING MENU")
    print("1. Search by TYPE")
    print("2. Search by NAME")
    print("3. Search by MEANING")
    print("4. EXIT")

    search_type = input("\nHow would you like to search today? [1-4]: ")

    #using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4"]:
        print("***INVALID ENTERY!***\nPlease try again")

    elif search_type == "1":
        print(f"You have chosen to search by TYPE")

        search = input("Which type: 'dragon' or 'elf':")

        if search not in ["dragon","elf"]: 
            #could also be: if search.title() not in class_type:
            print("***INVALID ENTERY!***\nPlease try again")
        else:
            found = []
            for i in range(0, len(class_type)):
                if search.lower() == class_type[i].lower():
                    found.append(i)

            if not found:
                print(f"Sorry, your search for {search} could not be completed.")
            else:
                print(f"Your search for {search} is complete! Detail below:")
                display("x", found, len(found))

    elif search_type == "2":
        
        for i in range(0, len(name) - 1):#outter loop
            for index in range(0, len(name) - 1):#inner loop
              #below if statement determines the sort
            #list used is the list being sorted
            # > is for increasing order, < for decreasing

                if(name[index] > name[index + 1]):
            #if above is true, swap places!
                   swap(index, name)
                   swap(index, class_type)
                   swap(index, meaning)
                   swap(index, culture)

        display("x", 0, len(name))

        #binary search
        search = input("Enter the NAME you are looking for: ")

        min = 0
        max = len(name) - 1
        mid = int((min + max)/2)

        while min < max and search != name[mid]:
            if search < name[mid]:
                max = mid - 1
            else:
                #search > name[mid]
                min = mid + 1
        mid = int((min + max)/2)

        if search == name[mid]:
            display(mid, 0, len(name))
        else:
            print(f"Your search for {search} came up empty.")


    elif search_type == "3":
        print(f"\nYou have chosen search by MEANING")

        search = input("Which name meaning are you looking for:").lower()

        found = []

        for i in range(0, len(meaning)):
            if search.lower() in meaning[i].lower():
                found.append(i)

        if not found:
            print(f"Sorry, we have names related to the meaning you entered:'{meaning}'")
        else:
            display("x",found, len(found))
    #Leave menu and close program
    elif search_type == "4":
        ans = "n"