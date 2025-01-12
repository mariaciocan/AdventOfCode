
from collections import defaultdict

def firstQuestion(rows):
    directions = [(1,0),(0,1),(-1, 0),(0, -1),(1,1),(-1,1),(-1,-1),(1,-1)] 
    lines = len(rows)
    columns = len(rows[0])
    xmas = 0
    for i in range(lines):
        for j in range(columns):
            elem = rows[i][j]
            if elem != "X":
                continue 
            for (dir_x, dir_y) in directions:
                if findXmas(i + dir_x, j+dir_y, rows, "M") and findXmas(i + 2 * dir_x, j + 2 * dir_y, rows, "A") and findXmas(i+ 3 * dir_x, j + 3 * dir_y, rows, "S"):
                    xmas += 1
    return xmas

def findXmas(i, j, rows, letter):
        lines = len(rows)
        columns = len(rows[0])
        if i < 0 or i >= lines or j < 0 or j >= columns:
            return False
        if rows[i][j] == letter:
            return True
        return False

def findAmas(i, j, rows):
    max_i = len(rows)
    max_j = len(rows[0])
    if i + 1 >= max_i or i-1 < 0 or j+1 >= max_j or j-1 < 0:
        return False
    if rows[i+1][j+1] == "S":
        if rows[i-1][j-1] != "M":
            return False
    elif rows[i+1][j+1] == "M":
        if rows[i-1][j-1] != "S":
            return False
    else:
        return False
    if rows[i+1][j-1] == "S":
        if rows[i-1][j+1] != "M":
            return False
    elif rows[i+1][j-1] == "M":
        if rows[i-1][j+1] != "S":
            return False
    else: 
        return False
    return True
    


with open('./input.txt') as f:
    data = f.read()
    rows = data.split('\n')
    xmas1 = firstQuestion(rows)
    xmas2 = 0
    lines = len(rows)
    columns = len(rows[0])
    for i in range(lines):
        for j in range(columns):
            if rows[i][j] == "A":
                if findAmas(i,j,rows):
                    xmas2 += 1
    print(xmas2)



        