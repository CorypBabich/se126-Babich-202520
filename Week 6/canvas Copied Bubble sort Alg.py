
name = "Jorge"

for i in range(0, len(name) - 1):#outter loop
    print("OUTER LOOP! i = ", i)


    for index in range(0, len(name) - 1):#inner loop
        print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort

        #list used is the list being sorted

        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):

            print("\t\t SWAP! ", name[index], "<-->", name[index + 1])

            #if above is true, swap places!

            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp


