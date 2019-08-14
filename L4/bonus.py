def compare_x(a1,a2,c2):
    if a2[0]<c2[0]:
        if (a1[0] in range(a2[0],c2[0]+1)):
            x = True
        else:
            x = False
    if a2[0]>c2[0]:
        if (a1[0] in range(c2[0],a2[0]+1)):
            x = True
        else:
            x = False
    return x

def compare_y(a1,a2,c2):
    if a2[1]<c2[1]:
        if (a1[1] in range(a2[1],c2[1]+1)):
            y = True
        else:
            y = False
    if a2[1]>c2[1]:
        if (a1[1] in range(c2[1],a2[1]+1)):
            y = True
        else:
            y = False
    return y

a1 = []
c1 = []
a2 = []
c2 = []
z = [a1,c1,a2,c2]
prompt = ["a1","c1","a2","c2"]
for i in range(0,4):
    x = int(input("coordinates of angle %s\n"%prompt[i]))
    y = int(input())
    z[i].append(x)
    z[i].append(y)

print(a1,c1,a2,c2)

a = (compare_x(a1,a2,c2)) and (compare_y(a1,a2,c2))
b = (compare_x(c1,a2,c2)) and (compare_y(c1,a2,c2))
c = (compare_x(a1,a2,c2)) and (compare_y(c1,a2,c2))
d = (compare_x(c1,a2,c2)) and (compare_y(a1,a2,c2))

if (a or b or c or d) == True:
    print("the rectangles overlap")
else:
    print("the rectangles don't overlap")
    
