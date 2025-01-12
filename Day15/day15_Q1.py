

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

def count_boxes(map):
    lines, columns = len(map), len(map[0])
    boxes = 0
    for i in range(lines):
        for j in range(columns):
            if map[i][j] == 'O':
                boxes += 1
    return boxes
def can_move_box(map, bi, bj, dirx, diry):
    lines, columns = len(map), len(map[0])
    while in_bounds(map, bi, bj) and map[bi][bj] != '.' and map[bi][bj] != '#':
        bi += dirx
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
    print(map)
    print(arrows)
    print(f"Boxes in the beginning: {count_boxes(map)}")
    rx, ry = find_robot_start(map)
    for arrow in arrows:
        dx, dy = directions[arrow]
        if not in_bounds(map, rx + dx, ry + dy):
            continue 
        if map[rx + dx][ry + dy] == '.':
            map[rx][ry] = '.'
            rx, ry = rx + dx, ry + dy
            map[rx][ry] = '@'
        else: 
            can_move, ki, kj = can_move_box(map, rx + dx, ry + dy, dx, dy)
            if can_move:
                if dx == 0:
                   if kj > ry:
                       while kj > ry: 
                           map[ki][kj] = map[ki][kj-1]
                           kj -= 1
                   else: 
                       while kj < ry:
                           map[ki][kj] = map[ki][kj+1]
                           kj += 1
                else: # dy == 0
                    if ki > rx:
                        while ki > rx:
                            map[ki][kj] = map[ki - 1][kj]
                            ki -= 1
                    else:
                        while ki < rx:
                            map[ki][kj] = map[ki + 1][kj]
                            ki += 1
                map[rx][ry] = '.'
                rx, ry = rx + dx, ry + dy
                map[rx][ry] = '@'

    lines, columns = len(map), len(map[0])
    print(f"Boxes in the end: {count_boxes(map)}")
    total = 0
    for i in range(lines):
        for j in range(columns):
            if map[i][j] == 'O':
                total += 100 * i + j
    print(total)
    
    


        
