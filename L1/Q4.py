y = input("please enter the year\n")
if float(y)%1 != 0:
    print ("invalid year")
elif int(y)%4 == 0 :
    print ("Yes, it is a leap year")
else:
    print ("No, it is not a leap year")
    
