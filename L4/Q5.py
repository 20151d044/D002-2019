def printer(secret, opened):
    i = 0
    while i < len(secret):
        if i in opened:
            print(secret[i],end="")
        else:
            print("_",end="")
        i = i + 1
    print("")
    

printer("apple", [1, 2]) # _pp__
printer("orange", [0, 5]) # o____e
printer("cat", []) # ___
