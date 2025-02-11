#Cory Babich
#W4D2 
#SE126.06
#1-28-2025 [W4D2]

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

def sort(list):
    for i in range(0, len(title) - 1):#outter loop
            for index in range(0, len(title) - 1):#inner loop
              #below if statement determines the sort
            #list used is the list being sorted
            # > is for increasing order, < for decreasing

                if(list[index] > list[index + 1]):
            #if above is true, swap places!
                   swap(index, bookNum)
                   swap(index, title)
                   swap(index, author)
                   swap(index, genre)
                   swap(index, pageCount)
                   swap(index, status)

        display("x", 0, len(list))

#--------MAIN EXECUTING CODE----------------------------------

bookNum = [] 
title = []
author = [] 
genre = []
pageCount = []
status = []
userInput = ""
continueY = "Y"

with open("Week 4 Homework/got_emails.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    for rec in file:
        bookNum.append(rec[0])
        title.append(rec[1])
        author.append(rec[2]) 
        genre.append(rec[3])
        pageCount.append(rec[4])
        status.append(rec[5])
        
while(continueY == "Y"):
    print("Personal Library Menu")
    print("1. Show All Titles – list all book data to the user alphabetically by title \n2. Search by Title – allow for an entire title or a title key word")
    print("3. Search by Author – show all titles of the searched-for author \n4. Search by Genre - show all titles of the searched-for genre \n5. Search by Library Number – only allow for one specific library number item")
    print("6. Show All Available – show all titles with status 'available' \n7. Show All On Loan - show all titles with status 'on loan' \n8. EXIT")
    userInput = input(" -: ")

    print()#print new line for readability

    if (userInput == "1"):
    #Show All Titles – list all book data to the user alphabetically by title
        for i in range(0, len(title)):
            print(f"")

    elif (userInput == "2"):
    #Search by Title – allow for an entire title or a title key word
        searchTitle = input("Enter the title you are looking for : ")
        

    elif (userInput == "3"):
    #Search by Author – show all titles of the searched-for author

    elif (userInput == "4"):
    #Search by Genre - show all titles of the searched-for genre

    elif (userInput == "5"):
    #Search by Library Number – only allow for one specific library number item

    elif (userInput == "6"):
    #Show All Available – show all titles with status “available”

    elif (userInput == "7"):
    #Show All On Loan - show all titles with status “on loan”

    elif (userInput == "8" or userInput.upper() == "EXIT"):
        continueY = "N"
    else:
        print("\n!!!INVALID INPUT!!!\n")
        print("")




