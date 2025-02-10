#Cory Babich
#W4D2 
#SE126.06
#1-28-2025 [W4D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------



#--------MAIN EXECUTING CODE----------------------------------

bookNum = [] 
title = []
author = [] 
genre = []
pageCount = []
status = []


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
        
print("Personal Library Menu")
print("1. Show All Titles – list all book data to the user alphabetically by title \n2. Search by Title – allow for an entire title or a title key word")
print("3. Search by Author – show all titles of the searched-for author \n4. Search by Genre - show all titles of the searched-for genre \n5. Search by Library Number – only allow for one specific library number item")
print("6. Show All Available – show all titles with status 'available' \n7. Show All On Loan - show all titles with status 'on loan' \n8. EXIT")








