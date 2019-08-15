def print_map(map):
    print("-" *25)
    for i in range(0, 6):
            for j in range(0, 6):
                print("| %s " % map[i][j], end="")
            print("|")
            print("-" * 25)
def get_input():
    global map
    while True:
         try:        
            col = int(input("Please enter column"))
            row = int(input("Please enter row"))
            no=int(input("Please enter the no."))
            if col>5 or col<0 or row>5 or row<0:
                print("enter again")
                continue
            if map[row][col] == '_':
                map[row][col] = no
                break
            elif input("It is taken already,sure to change?") == "yes":
                map[row][col] = no
                break
            else:
                print("enter again")
         except:
              continue
def check(map):
    if check_col(map) and check_row(map) and check_square(map):
         return True
    return False
def check_row(map):
    for i in range(0,6):
        list=[]
        if sum(map[i]) == 21:
            for x in range(0,6):
                if map[i][x] not in list:
                    list+=[map[i][x]]
                else:
                    return False
    return True
def check_col(map):
    for x in range (0,6):
        list=[]
        sum=0
        for i in range(0,6):
            sum+=map[i][x]
            if map[i][x] not in list:
                list+=[map[i][x]]
            else:
                return False
            if sum != 21:
                return False
    return True
def check_square(map):
    if sum(map)== 126:
        for i in range(1,7):
            if map.count(i) == 6:
                return True
            else:
                return False
    else:
        return False        
map=[["_","_","_","_","_","_"],
     ["_","_","_","_","_","_"],
     ["_","_","_","_","_","_"],
     ["_","_","_","_","_","_"],
     ["_","_","_","_","_","_"],
     ["_","_","_","_","_","_"]]
print_map(map)
while True:
    get_input()
    print_map(map)
    if check(map) ==  True:
        print("win")
        break
    
