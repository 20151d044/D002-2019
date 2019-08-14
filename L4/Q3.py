def factor(n):
    result = []
    for x in range(1, n + 1):
        if n % x == 0:
            result.append(x)
    return result


print(factor(40))  # prints [1, 2, 4, 5, 8, 10, 20, 40]
a = factor(30)
print(a)
if 5 in a:
     print("5 is a factor of 30") # it prints!

