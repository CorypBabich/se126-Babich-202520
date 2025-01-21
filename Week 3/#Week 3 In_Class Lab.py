#Cory Babich
#W3D2 - Week 3 In_Class Lab
#SE126.06
#1-21-2025 [W3D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import csv

#--FUNCTIONS-------------------------------------
  

#--Main Executing Code---------------------------

with open("Week 3/filehandling-1.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    types = []
    brands = []
    cpu = []
    ram = []
    disk1 = []
    numHDD = []
    disk2 = []
    os = []
    year = []
    deskNum = 0
    lapNum = 0
    deskCost = 0
    lapCost = 0

    for rec in file:
        if(rec[0].upper() == "D"):
            types.append("Desktop")
        elif(rec[0].upper() == "L"):
            types.append("Laptop")

        #determine the brand
        if(rec[1] == "DL"):
            brands.append("DELL")
        elif(rec[1] == "GW"):
            brands.append("Gateway")
        else:
            brands.append(rec[1])

        #record cpu, ram, 1st Disk, and HDD number info
        cpu.append(rec[2])
        ram.append(rec[3])
        disk1.append(rec[4])
        numHDD.append(rec[5])

        if len(rec) == 8:
            disk2.append("     ")
            os.append(rec[6])
            year.append(rec[7])
            if int(rec[7]) < 17:
                if(rec[0].upper() == "D"):
                    deskNum += 1
                    deskCost += 2000
                elif(rec[0].upper() == "L"):
                    lapNum += 1
                    lapCost += 1500
        elif len(rec) == 9:
            disk2.append(rec[6])
            os.append(rec[7])
            year.append(rec[8])
            if int(rec[8]) < 17:
                if(rec[0].upper() == "D"):
                    deskNum += 1
                    deskCost += 2000
                elif(rec[0].upper() == "L"):
                    lapNum += 1
                    lapCost += 1500

print(f"\n")
print(f"To replace {deskNum:2} desktops, it would cost ${deskCost:.2f}")
print(f"To replace {lapNum:2} desktops, it would cost ${lapCost:.2f}")
print(f"\n{"Type":7} \t {"Brand":7} \t {"CPU":5} \t {"RAM":5} \t {"1st Disk":7} \t {"NO HDD":7} \t {"2nd Disk":8} \t {"OS":5} \t {"YR":5}")
print("-----------------------------------------------------------------------------------------------------------")
for i in range(len(types)):
    print(f"{types[i]:7} \t {brands[i]:7} \t {cpu[i]:5} \t {ram[i]:5} \t {disk1[i]:7} \t {numHDD[i]:7} \t {disk2[i]:8} \t {os[i]:5} \t {year[i]:5}")

