#Cory Babich
#Lab 7
#SE126.06
#3-3-2025 [W8D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------



#--MAIN EXECUTING CODE----------------------------------

continueY = "Y"
userInput = ""
diction = {}

with open("Week 8 Homework/words.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    for rec in file:
        diction.update({rec[0]:rec[1]})

while continueY == "Y":
    print("1. Show all words – Show all words stored to the dictionary")
    print("2. Search for a word – Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if the word is not in the dictionary)")
    print("3. Add a word – Allow a user to add a word to the dictionary if it does not already exist\n4. EXIT")
    userInput = input("-:")

    if userInput == "1":
        print()
        for key in diction:
            print(f"{key:14}:{diction[key]}")
        print()
    elif userInput == "2":
        print()
        found = []
        search = input("What word would you like to find :")
        for key in diction:
            if search.upper() in key.upper():
                found.append(key)
        
        if len(found) > 1:
            print(f"We found these words with these definitions matching ({search})")
            for i in range(0,len(found)):
                print(f"{found[i]:14}:{diction[found[i]]}")
        elif found:
            print(f"We found this word and definition matching ({search})")
            print(f"{found[0]:14}:{diction[found[0]]}")
        else:
            print(f"The word {search} is not in this database.")

        print() #newline for readability
    elif userInput == "3":
        print()
        userWord = input("What is the word you would like to add :")
        userDef = input("What is the definition of the added word :")
        diction.update({userWord:userDef})
    elif userInput == "4":
        continueY = "N"
    else:
        print("***INVALID INPUT***")

print("Goodbye, and have a good day.")

