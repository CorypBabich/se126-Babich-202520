#Cory Babich
#SE126.06
#2-17-2025 [W6D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------

def display(x, foundList, records):
    '''
    x  =======  is passed the index

    records  =  is the length of the list we are going to process throguh (number of loops/prints)
    '''

    print(f"{'NUMBER':6} {'TITLE':34} {'AUTHORS':15} {'GENRE':15} {'PAGE#':6} {'STATUS'}")
    print(f"------------------------------------------------------------------------------------------------------")
    if x != "x":
        print(f"{bookNum[x]:6} {title[x]:34} {author[x]:15} {genre[x]:15} {pageCount[x]:6} {status[x]}")
    elif foundList: 
        for i in range(0, records):
            print(f"{bookNum[foundList[i]]:5} {title[foundList[i]]:34} {author[foundList[i]]:15} {genre[foundList[i]]:15} {pageCount[foundList[i]]:6} {status[foundList[i]]}")
    else:
        for i in range(0, records):
            print(f"{bookNum[i]:6} {title[i]:34} {author[i]:15} {genre[i]:15} {pageCount[i]:6} {status[i]}")

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

#checkes each element of the given list against the given string.
def find(search, field):
    indexes = [] #the lindexes where the list element matched the search value, to be passed to display

    for i in range(0, len(title)):
        if search.upper() in field[i].upper(): #if the search value is within the list element in foucs, append it to indexes 
            indexes.append(i)                   

    if not indexes:
        return("ERROR") #If the search value is not found, "ERROR" with be returned.
                        #If the search value is found, no value is returned and indexes is passed to display
    elif len(indexes) == 1:    
        display(indexes[0], 0, 0)
    else:
        display("x", indexes, len(indexes))

#checkes each element of the given list against the given string. Can only find Exact match
def findExact(search, field):
    index = [""] #the lindex where the list element matched the search value, to be passed to display

    for i in range(0, len(title)):
        if search.upper() == field[i].upper(): #if the search value is within the list element in foucs, append it to indexes 
            index[0] = i                   

    if index == 0:
        return("ERROR") #If the search value is not found, "ERROR" with be returned.
                        #If the search value is found, no value is returned and indexes is passed to display
    else:    
        display(index[0], 0, 0)

#--------MAIN EXECUTING CODE----------------------------------

bookNum = [] 
title = []
author = [] 
genre = []
pageCount = []
status = []
userInput = ""
continueY = "Y"

with open("Week 6 HomeWork/book_list.csv") as csvfile:

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
    print(f"")# print new line for readability

    print("Personal Library Menu")
    print("1. Show All Titles – list all book data to the user alphabetically by title \n2. Search by Title – allow for an entire title or a title key word")
    print("3. Search by Author – show all titles of the searched-for author \n4. Search by Genre - show all titles of the searched-for genre \n5. Search by Library Number – only allow for one specific library number item")
    print("6. Show All Available – show all titles with status 'available' \n7. Show All On Loan - show all titles with status 'on loan' \n8. EXIT")
    userInput = input(" -: ")

    print()#print new line for readability

    if (userInput == "1"):
    #Show All Titles – list all book data to the user alphabetically by title
        sort(title)

    elif (userInput == "2"):
    #Search by Title – allow for an entire title or a title key word
        searchTitle = input("Enter the title you are looking for : ")
        if find(searchTitle, title) == "ERROR":
            print(f"\n----We're sorry, No book Titled '{searchTitle}' could be found in our database----")

    elif (userInput == "3"):
    #Search by Author – show all titles of the searched-for author
        searchAuthor = input("Enter the author you are looking for : ")
        if find(searchAuthor, author) == "ERROR":
            print(f"\n----We're sorry, No book by {searchAuthor} could be found in our database----")

    elif (userInput == "4"):
    #Search by Genre - show all titles of the searched-for genre
        searchGenre = input("Enter the genre you are looking for : ")
        if find(searchGenre, genre) == "ERROR":
            print(f"\n----We're sorry, Our database does not contain a books in the {searchGenre} genre----")

    elif (userInput == "5"):
    #Search by Library Number – only allow for one specific library number item
        searchNum = input("Enter the Book Number of the book you are looking for : ")
        if findExact(searchNum, bookNum) == "ERROR":
            print(f"\n----We're sorry, Our database does not contain a books with the {searchNum} Book Number----")
    
    elif (userInput == "6"):
    #Show All Available – show all titles with status “available”
        find("available", status)

    elif (userInput == "7"):
    #Show All On Loan - show all titles with status “on loan”
        find("on loan", status)

    elif (userInput == "8" or userInput.upper() == "EXIT"):
        continueY = "N"
    else:
        print("\n!!!INVALID INPUT!!!\n")
        print("")

print("Goodbye, and have a good day!\n")


