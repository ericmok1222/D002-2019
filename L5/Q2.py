# Tic-Tac-Toe

def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)


def check_col(cells):
    for i in range(0, 3):
        if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
            return True
    return False
def check_row(cells):
    for i in range(0,3):
        if cells[i][0]== cells[i][1] == cells[i][2] != ' ':
            return True
    return False
def check_diagonal(cells):
    row =[[cells[0][2],cells[2][0]],[cells[0][0],cells[2],[2]]]
    for i in range(0,2):
        if cells[2][2] == row[i][0] == row[i][1]!=" ":
            return True
    return False
def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False
def get_input(symbol):
    global cells
    while True:
        col = int(input("%s Please enter column"%symbol))
        row = int(input("%s Please enter row"%symbol))
        if cells[row][col] == ' ':
            cells[row][col] = symbol
            break
        else:
            print("It is taken already")


    

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
symbol=["x","o"]
printcell(cells)
while True:
    get_input(symbol[0])
    printcell(cells)
    if check(cells) ==  True:
        print("%s win"%symbol[0])
        break
    get_input(symbol[1])
    printcell(cells)
    if check(cells) ==  True:
        print("%s win"%symbol[1])
        break
