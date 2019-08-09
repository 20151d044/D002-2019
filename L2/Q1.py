x = int (input ("input a positive integer \n"))
y = 3

if x%2 == 0 :
     print ("it is not a prime number as it is divisible by 2")
     
     
while y <= x/2 and x%2 != 0  :
    
    if x % y == 0 :
        print ("it is not a prime number as it is divisible by %d"%y)
        break

    else :
        print ("%d=false"%y)
        y = y+2
        
if y >= x/2 :
    print ("it is a prime number")
    

