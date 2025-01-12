
from collections import defaultdict
from math import sqrt, pow


def distance_between_points(a, b, c, d):
    return sqrt((a * a - c * c) + (b * b - d * d))

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
                freq[line[i]].append((lines, i))
        lines += 1
    marked = set()
    points = 0
    for antenna in list(freq.keys()):
        positions = freq[antenna]
        for i in range(len(positions) - 1):
            curr_i, curr_j = positions[i][0], positions[i][1]
            for j in range(i+1, len(positions)):
                second_i, second_j = positions[j][0], positions[j][1]
                diff_i = (second_i - curr_i)
                diff_j = (second_j - curr_j)
                if in_bounds(curr_i - diff_i, curr_j - diff_j, matrix) and ((curr_i - diff_i), (curr_j - diff_j)) not in marked:
                    points += 1
                    marked.add((curr_i - diff_i, curr_j - diff_j))
                if in_bounds(second_i + diff_i, second_j + diff_j, matrix) and ((second_i + diff_i, second_j + diff_j)) not in marked:
                    points += 1
                    marked.add((second_i + diff_i, second_j + diff_j))
    print(points)