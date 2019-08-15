grid1 = [['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o']]
grid2 = [['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o'],['o','o','o','o','o','o','o','o','o','o']]
grid = [grid1,grid2]

def printer(player):
    for u in range(0,10):
        for i in range(0,10):
            print(grid[player][u][i],end='')
        print("\n",end="")

def setup(no_cells,no_boats,player):
    a = 1
    while a <= no_boats:
        print("enter the coordinates of the front of the boat occupying %d cells"%no_cells)
        row = int(input("row="))
        col = int(input("column="))
        dir = input("choose the diection its back faces by entering \"wasd\"")
        a = a+1
        if dir == "w":
            for b in range(0,no_cells):
                grid[player][row-b][col] = "x"
        if dir == "a":
            for b in range(0,no_cells):
                grid[player][row][col-b] = "x"
        if dir == "s":
            for b in range(0,no_cells):
                grid[player][row+b][col] = "x"
        if dir == "d":
            for b in range(0,no_cells):
                grid[player][row][col+b] = "x"
        printer(player)
        print(a)


printer(1)
for c in range (0,2):
    setup(4,1,c)
    setup(3,2,c)
    setup(2,3,c)
    setup(1,4,c)

        
"""
seems working
but error checking inside setup for input is unseccessful arrrrrrrr QAQ
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

    










