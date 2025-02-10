# Cory Babich


import csv

lib_num = []
titles = []
authors = []
genres = []
pages = []

with open("Week 6/library_books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        lib_num.append(rec[0])
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])

print(f"{'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':20} {'PAGES':5}")
print("--------------------------------------------------------------------")
for i in range(0,len(lib_num)):
    print(f"{lib_num[i]:5} {titles[i]:25} {authors[i]:15} {genres[i]:20} {pages[i]:5}")
print("----------------------------------------------------------------------")



found = []
#search_Title = input("La dee da : ")
search_Num = input("NUMBER! GIVE NUMER : ")
seq_count = 0

#for i in range(0,len(titles)):
#    if search_Title.lower() in titles[i].lower:
#        found.append(i)

for i in range(0, len(lib_num)):
    seq_count += 1
    if search_Num in lib_num[i]:
        found.append(i)

print(f"searched: {seq_count}")
if not found:
    print(f"Sorry, your search for {search_Num} was not found.")
else:
    print(f"Your search for {search_Num} was FOUND!")

    print(f"{'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':20} {'PAGES':5}")
    print("--------------------------------------------------------------------")
    for i in range(0,len(found)):
        print(f"{lib_num[found[i]]:5} {titles[found[i]]:25} {authors[found[i]]:15} {genres[found[i]]:20} {pages[found[i]]:5}")
    print("----------------------------------------------------------------------")


#Binary Search

min = 0 
max = len(lib_num) - 1
mid = int((min + max) / 2)

bin_count = 0

while min < max and search_Num != lib_num[mid]:
    #If min is ever equal to max, search options have been exhausted
    #If search_num is eaver equal to lib_num[mid], we have found our requested search 

    if search_Num < lib_num[mid]:
        max  = mid - 1
    else:
        min = mid + 1
    
    mid = int((min + max) / 2)
    bin_count += 1
        
print(f"BINARY SEARCH ITERATIONS: {bin_count}")

if search_Num == lib_num[mid]:
    print(f"Your search for {search_Num} was Found!")
    print(f"{'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':20} {'PAGES':5}")
    print("--------------------------------------------------------------------")
    print(f"{lib_num[mid]:5} {titles[mid]:25} {authors[mid]:15} {genres[mid]:20} {pages[mid]:5}")
    print("----------------------------------------------------------------------")
else:
    print(f"Not found :()")    

