grid1 = [['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o']]
grid2 = [['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o']]
grid = [grid1,grid2]

def printer(player):
    for u in range(0,10):
        for i in range(0,10):
            print(grid[player][u][i],end='')
        print("\n",end="")

def check(dir,no_cells,row,col,player):
    if dir == "r":
        for r in range(0,no_cells):
            if ((grid[player][row+1][col+r]) or (grid[player][row-1][col+r])) == "x":
                return True
            else:
                return False
    if dir == "d":
        for r in range(0,no_cells):
            if ((grid[player][row+r][col+1]) or (grid[player][row+r][col-1])) == "x":
                return True
            else:
                return False

"""
def check(no_cells,player):
    for r in range(0,10):
        for c in range(0,10):
            if grid[player][r][c] == "v":
                if (grid[player][r][c+1] or grid[player][r][c-1] or grid[player][r+1][c] or grid[player][r-1][c]) == "x":
                    return False
                else:
                    return True
"""


def setup(no_cells,no_boats,player):
    a = 1
    while a <= no_boats:
        print("enter the coordinates of the front of the boat occupying %d cells"%no_cells)
        row = int(input("row="))
        col = int(input("column="))
        dir = input("put the ship in the direction of (r)ight or (d)own?\n")
        if dir == "d":
            if row > 10-no_cells:
                continue
            elif check(dir,no_cells,row,col,player) == True:
                continue
            else:
                for b in range(0,no_cells):
                    grid[player][row+b][col] = "x"
                    
        if dir == "r":
            if col > 10-no_cells:
                continue
            elif check(dir,no_cells,row,col,player) == True:
                continue
            else:
                for b in range(0,no_cells):
                    grid[player][row][col+b] = "x"

        else:
            continue      
        a = a+1
        printer(player)
        print(a)
    

def guess(player):
    print("Hit on point now!")
    row = int(input("row=\n"))
    col = int(input("column=\n"))
    if grid[(player+1)%2][row][col] == "x":
        print("You hit a boat!")
        
        printer(1)

            


printer(1)
for c in range (0,2):
    print("you are player %d"%c)
    setup(4,1,c)
    setup(3,1,c)
    setup(2,3,c)
    setup(1,4,c)

guess(0)




        
"""
seems working
but error checking inside setup for input is unseccessful arrrrrrrr QAQ
gave up on the first two lines
later solve la
also haven't finished all the errors
tmr sin finish during class maybe
im so sleepy la_zzzzz
        if ((row or col) not in range (0,10)) or (dir != ("w","a","s","d")):
            print("invalid input")
            continue
"""

"""
ask user to input the cooedinates they want to bomb
then replace the checked empty cells with +(?) ~easier to count
(x=have boat,o=nth,+=havent shown)
then i have no idea what to do next la @_@
"""

    










