y = 0
for a in range(1,57):
    for b in range(1,60-2-a):
        for c in range(1,60-1-a-b):
            d = 60-a-b-c
            x = a*b+b*c+c*d
            if y == 0:
                y = x
            if x > y:
                y = x
                A = a
                B = b
                C = c
                D = d
                
print("maxium value of ab+bc+cd is %d"%y)
print("a=%d"%A)
print("b=%d"%B)
print("c=%d"%C)
print("d=%d"%D)

#print("a=%d\nb=%d\nc=%d\nd=%d"%A%B%C%D)

            
            
