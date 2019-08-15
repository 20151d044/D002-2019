cells = [[" "," "," "],[" "," "," "],[" "," "," "]]

def printer():
    for u in range(0,3):
        print("-"*13)
        for i in range(0,3):
            print("| %s "%cells[u][i],end="")
        print("|")
    print("-"*13)

def check_col():
    for i in range(0,3):
        if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
            return True
        elif i == 2:
            return False

def check_row():
    for i in range(0,3):
        if cells[i][0] == cells[i][1] == cells[i][2] != ' ':
            return True
        elif i == 2:
            return False

def check_diagonal():
    for i in range(0,2):
        if cells[0][0] == cells[1][1] == cells[2][2] != ' 'or cells[0][2] == cells[1][1] == cells[2][0]:
            return True
        elif i == 1:
            return False
full = False
printer()
p = ["x","o"]
while (check_col() and check_row() and check_diagonal()) == False and full == False:
    for a in range(0,2):
        for b in range (0,3):
            for c in range (0,3):
                if cells[b][c] == ' ':
                    full = False
        if ((check_col() and check_row() and check_diagonal()) == False) and (full == False):
            row = int(input("you are %s, please place your symbol\nrow ="%p[a]))
            col = int(input("column ="))
            while cells[row-1][col-1] != " " or (row or col) not in range(1,4):
                print("invalid input")
                row = int(input("row ="))
                col = int(input("column ="))
                if cells[row-1][col-1] == " ":
                    break
            cells[row-1][col-1] = p[a]
            printer()
        else:
            break
    

if full != False:
    print("draw")
else:
    print("game over")


        

    


