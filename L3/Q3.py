list = []
print("please type 10 words starting with capital letters")
for n in range(0,11):
    w = input()
    if w[0]=="A" or w[0]=="E" or w[0]=="I" or w[0]=="O" or w[0]=="U":
        list.append(w)
print(list)
