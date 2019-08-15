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
        if cells[0][0] == cells[1][1] == cells[2][2] != ' 'or cells[0][2] == cells[1][1] == cells[2][0] != ' ':
            return True
        elif i == 1:
            return False
def check():
    if check_col() or check_row() or check_diagonal() == True:
        return True
    else:
        return False

p = ["x","o"]
n = 1
while check() == False and n <= 9:
    printer()
    row = int(input("you are %s, please place your symbol\nrow ="%p[n%2]))
    col = int(input("column ="))
    while cells[row][col] != " " or (row or col) not in range(0,3):
        print("invalid input")
        row = int(input("row ="))
        col = int(input("column ="))
    cells[row][col] = p[n%2]
    n = n+1

if n == 10:
    print("draw")
else:
    print("game over, %s wins"%p[n%2])
