def checker(sentence, letter):
    result = []
    index=0
    for i in sentence:
        if i == letter:
            result+=[index]
        index+=1
    return (result)
a = checker("Apple", "p") # a = [1, 2]
b = checker("Banana", "p") # b = []
c = checker("Cat", "a") # c = [1]

print(a,b,c)
