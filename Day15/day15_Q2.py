

import copy


def set_directions():
    directions = {}
    directions['^'] = (-1, 0)
    directions['v'] = (1, 0)
    directions['>'] = (0, 1)
    directions['<'] = (0, -1)
    return directions

def find_robot_start(map):
    lines, columns = len(map), len(map[0])
    for i in range(lines):
        for j in range(columns):
            if map[i][j] == '@':
                return (i, j)

def in_bounds(map, i, j):
    lines, columns = len(map), len(map[0])
    if i < 0 or i >= lines or j < 0 or j >= columns:
        return False
    return True

def print_map(map):
    for line in map:
        output.write(str(line))
        output.write('\n')

def resize_matrix(map):
    lines, columns = len(map), len(map[0])
    new_map = [['.' for _ in range(columns * 2)] for _ in range(lines)]
    new_j = 0
    for i in range(lines):
        new_j = 0
        for j in range(columns):
            if map[i][j] != '@':
                if map[i][j] in ['.', '#'] :
                    new_map[i][new_j], new_map[i][new_j + 1] = map[i][j], map[i][j]
                    new_j += 2
                else:
                    new_map[i][new_j], new_map[i][new_j + 1] ='[',  ']'
                    new_j += 2
            else:
                new_map[i][new_j] = '@'
                new_map[i][new_j + 1] = '.'
                new_j += 2
    return new_map

def count_boxes(map):
    lines, columns = len(map), len(map[0])
    boxes = 0
    for i in range(lines):
        for j in range(columns):
            if map[i][j] == '[':
                boxes += 1
    return boxes

def find_dot(map, i, j, j2, dx):
    while in_bounds(map, i + dx, j):
        if map[i + dx][j] == '.' or map[i+dx][j2] == '.':
            return i + dx
        i += dx
    return -1 

def move_paranthesis(map, i, j, dx):
    if map[i][j] == '[':
        if map[i+dx][j] == ']' or map[i+dx][j] == '[':
            move_paranthesis(map, i+dx, j, dx)
        if map[i+dx][j+1] == '[':
            move_paranthesis(map, i+dx, j+1, dx)
        map[i + dx][j] = '['
        map[i + dx][j + 1] = ']'
        map[i][j] = '.'
        map[i][j+1] = '.'
    else:
        if map[i+dx][j] == '[' or map[i+dx][j] == ']':
            move_paranthesis(map, i +dx,j,dx)
        if map[i+dx][j-1] == "]":
            move_paranthesis(map, i + dx, j-1, dx)
        map[i][j] = '.'
        map[i][j-1] = '.'
        map[i + dx][j] = ']'
        map[i + dx][j - 1] = '['
    return map

def can_move_paranthesis(map, i, j, dx, output):

    while in_bounds(map, i + dx, j):
        if map[i + dx][j] == '.':
            return True
        if map[i + dx][j] == '#':
            return False
        if map[i + dx][j] == '[':
            return can_move_paranthesis(map, i + dx, j, dx, output) and can_move_paranthesis(map, i + dx, j + 1, dx, output)
        else:
            return can_move_paranthesis(map, i + dx, j, dx, output) and can_move_paranthesis(map, i + dx, j - 1, dx, output)
    return False

def can_move_box_sideways(map, bi, bj, diry):
    bj += 1
    while in_bounds(map, bi, bj) and map[bi][bj] != '.' and map[bi][bj] != '#':
        bj += diry
    if not in_bounds(map, bi, bj) or map[bi][bj] == '#':
        return [False, -1, -1]
    return [True, bi, bj]
 
with open("input.txt") as input:
    map = []
    output = open('output.txt', 'w')
    second_input = False
    directions = set_directions()
    arrows = ''
    for line in input:
        if line == '\n':
            second_input = True
            continue
        if not second_input:
            map.append(list(line.strip()))
        else:
            arrows += (line.strip())
    map = resize_matrix(map)
 
    rx, ry = find_robot_start(map)
    for arrow in arrows:
        prior_map = copy.deepcopy(map)
        dx, dy = directions[arrow]
        if not in_bounds(map, rx + dx, ry + dy):
            continue 

        if map[rx + dx][ry + dy] == '.':
            map[rx][ry] = '.'
            rx, ry = rx + dx, ry + dy
            map[rx][ry] = '@'

        elif map[rx + dx][ry + dy] == '[' or map[rx + dx][ry + dy] == ']':
            if dx == 0: # moving sideways 
                can_move, ki, kj = can_move_box_sideways(map, rx + dx, ry + dy, dy)
                if can_move:
                    if kj > ry:
                        while kj > ry: 
                            map[ki][kj] = map[ki][kj-1]
                            kj -= 1
                    else: 
                        while kj < ry:
                            map[ki][kj] = map[ki][kj+1]
                            kj += 1
                    map[rx][ry] = '.'
                    rx, ry = rx + dx, ry + dy
                    map[rx][ry] = '@'
            else: # moving vertically 
                if map[rx + dx][ry + dy] == '[':
                    if can_move_paranthesis(map, rx + dx, ry + dy, dx, output) and can_move_paranthesis(map, rx + dx, ry + dy + 1, dx, output):
                        ki = find_dot(map, rx + dx, ry + dy, ry + dy + 1, dx)
                        if ki > rx + dx: # moving down 
                            while in_bounds(map, ki - 1, ry + dy) and ki > rx + dx:
                                if map[ki - 1][ry + dy] == '[' or map[ki -1][ry + dy] == ']':
                                    map = move_paranthesis(map, ki - 1, ry + dy, 1)
                                else:
                                    map[ki][ry + dy] = map[ki - 1][ry + dy]
                                ki -= 1
                        else: # moving up
                             while in_bounds(map, ki - 1, ry + dy) and ki < rx + dx:
                                if map[ki + 1][ry + dy] == '[' or map[ki + 1][ry + dy] == ']':
                                    map = move_paranthesis(map, ki + 1, ry + dy, -1)
                                else:
                                    map[ki][ry + dy] = map[ki + 1][ry + dy]
                                ki += 1
                        map[rx][ry] = '.'
                        rx, ry = rx + dx, ry + dy
                        map[rx][ry] = '@'
                elif map[rx + dx][ry + dy] == ']':
                    if can_move_paranthesis(map, rx + dx, ry + dy, dx, output) and can_move_paranthesis(map, rx + dx, ry + dy - 1, dx, output):
                        ki = find_dot(map, rx + dx, ry + dy, ry + dy - 1, dx)
                        if ki > rx + dx: # moving down
                            while in_bounds(map, ki - 1, ry + dy) and ki > rx + dx:
                                if map[ki - 1][ry + dy] == '[' or map[ki -1][ry + dy] == ']':
                                    map = move_paranthesis(map, ki - 1, ry + dy, 1)
                                else:
                                    map[ki][ry + dy] = map[ki - 1][ry + dy]
                                ki -= 1
                        else: # moving up
                             while in_bounds(map, ki + 1, ry + dy) and ki < rx + dx:
                                if map[ki + 1][ry + dy] == '[' or map[ki + 1][ry + dy] == ']':
                                    map = move_paranthesis(map, ki + 1, ry + dy, -1)
                                else:
                                    map[ki][ry + dy] = map[ki + 1][ry + dy]
                                ki += 1
                        map[rx][ry] = '.'
                        rx, ry = rx + dx, ry + dy
                        map[rx][ry] = '@'

    lines, columns = len(map), len(map[0])
    total = 0
    for i in range(lines):
        for j in range(columns):
            if map[i][j] == '[':
                total += 100 * i + j
    print(total)
    
    


        
