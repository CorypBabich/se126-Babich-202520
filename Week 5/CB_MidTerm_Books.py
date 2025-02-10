#Cory Babich
#W5D2 
#SE126.06
#2-4-2025 [W5D2]

#Prompt: Choice 2

#Prompt Summary: Read from a CSV file that has a data base of books, Copy the records into 1D lists, print each record to the sceen and record cound, 
#create and write to a new csv file, and create a Sequential search program for the data base that can search by title and author

#VARIABLE DICTIONARY

# title     Holds all the titles read from the csv file
# author -- Holds all the author names read from the csv file
# genre     Holds all the genres read from the csv file
# pages --- Holds all the book page counts read from the csv file
# status    Holds all the availability statuses assigned to each book in this program

# avail         determines the number of available books, by being declared as half the value of the length of title rounded.

# continueY     Is checked by the menu loop, if it is ever equal to 0 than the loop and the program end.
# userInput --- Holds the user's input on the main menu, and is check for which option the user wants.
# titleSearch   Holds the user's input for the title of the book they want to find.
# titleFound -- Holds the index of the book that matches the title given to titleSearch
# authorSearch  Holds the user's input for the name of the author they want to find.
# authorFound - Holds a list of index's for books that have an author that matches the author given to authorsearch

#file   Holds the contents of the csv file as a 2D list
#rec    Holds each record of file as a 1D list

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------

#--Main Executing Code---------------------------

title = []
author = []
genre = []
pages = []
bookCount = 0

with open("Week 5/books.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

#populating lists
    for rec in file:

        title.append(rec[0])
        author.append(rec[1])
        genre.append(rec[2])
        pages.append(rec[3])

status = []
avail = int(len(title)/2)

#asigning the book statuses, half of which are Available and the other half On Loan
for i in range(0, len(title)):
    if avail > 0:
        status.append("Available")
        avail -= 1
    else:
        status.append("On Loan")

#Print all records to sceen
print(f"{"Title":25}, {"Author":12}, {"genre":7}, {"Page Count":3}, {"Status"}")
print("--------------------------------------------------------------------------")

for i in range(0,len(title)):
    print(f"{title[i]:25}, {author[i]:12}, {genre[i]:7}, {pages[i]:3}, {status[i]}")
#Print the total number of books
print(f"There are {len(title)} Books in the data base.\n")

#Creating txt file and writing the lists to the file
file = open('midterm_choice2.csv','w') 
for i in range(0, len(title)):
    if i != (len(title)-1):
        file.write(f"{title[i]},{author[i]},{genre[i]},{pages[i]},{status[i]}\n")
    else:
        file.write(f"{title[i]},{author[i]},{genre[i]},{pages[i]},{status[i]}")
file.close()

#Sequential search and Menu
continueY = 1 #Continue check, set to 0 to end menu loop
userInput = ""
titleSearch = ""
titleFound = 0
authorSearch = ""
authorFound = []

#Seach Menu
print("Hello What can I help you find today?")#Menu Greeting
while continueY == 1:
    print("1. Search by Title\n2. Search by Author\n3. EXIT")#print Menu Options
    userInput = input(" :")
    print()

    #Search by title
    if userInput == "1":
        titleSearch = input("What is the Title of the book you are looking for : ")
        
        #search for given title
        for i in range(0, len(title)):
            if title[i].upper() == titleSearch.upper():
                titleFound = i
        
        #Report to user if book was found or not
        if titleFound != 0: #book found
            print("\nHere is the book you are looking for:\n")
            print(f"{"Title":25}, {"Author":12}, {"genre":7}, {"Page Count":3}, {"Status"}")
            print("--------------------------------------------------------------------------")
            print(f"{title[titleFound]}, {author[titleFound]}, {genre[titleFound]}, {pages[titleFound]}, {status[titleFound]}")
        else: #book not found
            print("\n ---We are Sorry---")
            print("A book by this title was not found, it might have been misspelled or doesn't exist in this database.")

        print("\nCan I help you find another book?")

    #search by author
    elif userInput == "2":
        authorSearch = input("What is the name of the author you are looking for : ")
        
        #search for given author
        for i in range(0, len(author)):
            if author[i].upper() == authorSearch.upper():
                authorFound.append(i)

        #Report to user if author was found or not
        if len(authorFound) != 0: #author found
            print(f"\nHere are books by the author you are looking for: We found {len(authorFound)} books\n")
            print(f"{"Title":25}, {"Author":12}, {"genre":7}, {"Page Count":3}, {"Status"}")
            print("--------------------------------------------------------------------------")
            for i in range(0, len(authorFound)):
                print(f"{title[authorFound[i]]:25}, {author[authorFound[i]]:12}, {genre[authorFound[i]]:7}, {pages[authorFound[i]]:3}, {status[authorFound[i]]}")
        else: #author not found
            print("\n ---We are Sorry---")
            print("A book by this author was not found, their name might have been misspelled (Remember to include a space between first and last name) \nor no books by this author are in this database.")

        print("\nCan I help you find another book?")
    
    #Exit the Program
    elif userInput == "3":
        continueY = 0
    
    #catch for if the user gives an unexpected input
    else:
        print("\n---INVALID INPUT---")
        print("Please enter the number that is next to your desired option '1' '2' '3' \n with no spaces before or after.\n")

#Goodbye message as the program closes
print("Goodbye, and have a great day.")




















