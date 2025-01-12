
from collections import defaultdict
from math import sqrt, pow

def in_bounds(x, y, matrix):
    l = len(matrix)
    c = len(matrix[0])
    if x < 0 or x >= l:
        return False
    if y < 0 or y >= c:
        return False
    return True

with open('./input.txt') as f:
    matrix = []
    freq = defaultdict(list)
    lines = 0
    equations = []
    for line in f:
        line = line.strip()
        matrix.append(line)
        for i in range(len(line)):
            if line[i] != '.':
                freq[line[i]].append((i, lines))
        lines += 1
    marked = set()
    points = 0
    slopes = defaultdict(list)
    for antenna in list(freq.keys()):
        positions = freq[antenna]
        for i in range(len(positions) - 1):
            curr_i, curr_j = positions[i][0], positions[i][1]
            for j in range(i+1, len(positions)):
                second_i, second_j = positions[j][0], positions[j][1]
                
                slope =  (second_j - curr_j) / (second_i - curr_i)
                b = curr_j - slope * curr_i
                for l in range(lines):
                    intersection = (l - b) / slope
                    if abs(intersection - round(intersection)) < 0.0001: #tolerance 
                        if in_bounds(round(intersection), l, matrix):
                            if (round(intersection), l) not in marked:
                                marked.add((round(intersection), l))
                                points += 1
    print(points)