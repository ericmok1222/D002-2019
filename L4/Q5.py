def printer(secret, opened):
    i = 0
    w="_"
    while i < len(secret):
        if i not in opened:
            print("_",end="") 
        else:
            print(secret[i],end="")
        i = i + 1

# Note: you might use print(x, end="") to print x without changing line
printer("apple", [1, 2]) # _pp__
print("\n")
printer("orange", [0, 5]) # o____e
print("\n")
printer("cat", []) # ___
