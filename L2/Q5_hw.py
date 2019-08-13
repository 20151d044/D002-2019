# L2 Q5: play rock-paper-scissor - Beat the King
# You need to win the king three times in a row in order to throw him away from his throne
# Carefully think about where a loop should be place
# Suggested Logic:
#
# Repeat the following until you really win
#        Challenge the king three times, in each challenge
#               pick a choice for the King and a choice for the player
#               Repeat this if it is draw
#                      pick a choice for the King and a choice for the player
#               if fail the challenge, break from this loop
#        




# Import necessary modules
from random import randint
wins = 0

print('Welcome to the rock-paper-scissor game!\nYou are going to play against a minion!')

# ascii art from https://www.asciiart.eu/people/body-parts/hand-gestures
print("Please input your choice")
print("""
1.                 2.                           3.
    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)
""") 
p_choice = int(input("1 for rock; 2 for paper; 3 for scissor"))

# step2: generate a random choice for minion, save it in variable m_choice 


# status is used for the win/lose/draw of the game
# status = 1 means player wins; status = 2 means minion wins; status = 3 means draw;
# status = 4 means user gives invalid input, e.g. player inputs -1 or 4
status = 0 # initialized as 0


while wins < 3:
    m_choice = randint(1,3)

    if p_choice not in range (0,4):
        status = 4
        print("please enter a valid choice")
        break
    
    if m_choice == 1:
        print("Minion chooses rock!")
    elif m_choice == 2:
        print("Minion chooses paper!")
    elif m_choice == 3:
        print("Minion chooses scissor!")
        
    if p_choice == m_choice:
        status = 3
        print("draw")
        p_choice = int(input("enter a new choice"))
        continue
    elif (p_choice ==2 and m_choice==1) or (p_choice ==3 and m_choice==2) or (p_choice ==1 and m_choice==3):
        status = 2
        wins = wins + 1
        if wins==3:
            break
        p_choice = int(input("you have won this round, please enter a new choice"))
        
    else:
        status = 1
        print("you lost this round, please play again")
        break


if wins == 3:
    print ("congratulations! you beat the minion!")
        
