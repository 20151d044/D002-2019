print("I got a %d" % number)
count = 1
while number!=6: # replace with your code
    # Write some more code
    print("I got a %d" % number)
    count = count + 1
    number = randint(1,6)
if number==6:
    print("I got a %d" % number)
    count = count+1

print("Oh, it takes me %d times to get a 6!!!" % count)


# d) How long it takes, in general?
# Repeat the experiment in part c for 100 times and see what is the average 
# value of the count would be. This is challenging, isn't it?

from random import randint

#code for rolling a dice
x = []
count = 1
number = randint(1,6)
for n in range(0,101):
    while number!=6:
        count = count+1
        number = randint(1,6)
    if number==6:
        x.append(count)
        print("value of count=%d"%count)
        count = 0
        number = 0

        
print("the average is %f"%((sum(x[0:100])/100)))
