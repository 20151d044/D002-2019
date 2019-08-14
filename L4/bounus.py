a1 = [5,8]
c1 = [10,1]
a2 = [-1,11]
c2 = [5,8]

if (a1[0] in range(a2[0],c2[0]+1)) and (a1[1] in range(a2[1],c2[1]+1)):
    print("it overlapps")
else:
    print("1")
if (c1[0] in range(a2[0],c2[0]+1)) and (c1[1] in range(a2[1],c2[1]+1)):
    print("it overlapps")
else:
    print("2")
    
    
    
