y = input("please enter the year\n")
if float(y)%1 != 0:
    print ("please enter a valid year")
elif int(y)%4 == 0 :
    print ("Yes, it is a leap year")
else:
    print ("No, it is not a leap year")
    
