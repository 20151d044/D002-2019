def checker(sentence, letter):
    result = []
    for i in range(0,len(sentence)):
              if sentence[i]==letter:
                  result.append(i)
    return result
                  
print(checker("applep","p"))    

