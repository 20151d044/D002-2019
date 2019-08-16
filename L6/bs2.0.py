grid1 = [['o','o','o','o','o','o','o','o','o','o',' ']*10,[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
grid2 = [['o','o','o','o','o','o','o','o','o','o',' '],['o','o','o','o','o','o','o','o','o','o',' '],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o']]
grid = [grid1,grid2]

def printer(player):
    for u in range(0,10):
        for i in range(0,10):
            print(grid[player][u][i],end='')
        print("\n",end="")
        
def check(dir,row,col,no_cells,player):
    if (dir == "r"):
        for i in range (col, col+no_cells+1):
            if i == col and col != 0:
                if grid[player][row][i-1] == "x":
                    return False
            if i == col+no_cells and col != 9:
                if grid[player][row][i+1] == "x":
                    return False
            if row != 0:
                if grid[player][row-1][i] == "x":
                    return False
            if row != 9:
                if grid[player][row][i+1] == "x":
                    return False
    if (dir == "d"):
        for i in range (row, row+no_cells+1):
            if i == row and row != 0:
                if grid[player][i-1][col] == "x":
                    return False
            if i == row+no_cells and row != 9:
                if grid[player][i+1][col] == "x":
                    return False
            if col != 0:
                if grid[player][i][col-1] == "x":
                    return False
            if col != 9:
                if grid[player][i][col+1] == "x":
                    return False
            
           

def setup(no_cells,no_boats,player):
    a = 1
    while a <= no_boats:
        check = True
        print("enter the coordinates of the front of the boat occupying %d cells"%no_cells)
        row = int(input("row="))
        col = int(input("column="))
        dir = input("put the ship in the direction of (r)ight or (d)own?\n")
        if dir == "d":
              if row > 10-no_cells:
                 continue
              elif check(dir,row,col,no_cells,player) == True:
                 for b in range(0,no_cells):
                  grid[player][row+b][col] = "x"
              else:
                  continue
                  
        if dir == "r":
            if col > 10-no_cells:
                continue
            elif check(dir,row,col,no_cells,player) == True:
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
    setup(4,1,c)
    setup(3,1,c)
    '''setup(2,3,c)
    setup(1,4,c) '''






        
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

    










