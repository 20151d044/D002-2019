#L2 Q6: Banana Guessing game

#Step 1: Import necessary modules
import random

#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')

#Step 3: Choose a random number between 1-100
n = random.randint(1,100)

# define a flag for found/not found and counter on how many trials
found = False
count = 0

#Step 4: Give three chances to the players 
for count in range(1,4):
    b = int(input("guess the number of bananas"))
    if b==n:
        found = True
        break
    elif b>n:
        found = False
        print("your guess is too high")
    elif b<n:
        found = False
        print("your guess is too low")
    else:
        print("your answer is out of the range of 1-100")
        
#Step 5: Display a message
print ("shhh, Dave hides %s bananas" % n)
if found == True:
        print('You got the correct guess in %d trials' % count)
        print('Dave\'s banana are now all yours!')
else:
        print("You failed to find the number of bananas Dave hid! Try again next")

