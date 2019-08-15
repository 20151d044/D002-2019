import random
word_list = ["apple","egg","carrot","bread","cat","library"]
secret = word_list[random.randint(0,len(word_list)-1)]
opened = []

opened.append("_"*len(secret))

def checker(secret,letter):
    for i in range (0,len(secret)):
        if secret[i] == letter : 
            opened[i] = letter
    return opened

print(opened)
while opened != secret:
    letter = input("input a letter")
    checker(secret,letter)
    print(opened)

print("cpngratulaitons, you won!")


