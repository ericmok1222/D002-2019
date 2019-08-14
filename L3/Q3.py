word=input("input word").split()
test = ["A","E","I","O","U","a","e","i","o","u"]
list=[]
for i in word:
    for x in test:
        if i[0] == x:
            list+=[i]
            continue
print(list)
            
