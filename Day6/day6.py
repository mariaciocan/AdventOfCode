def guard_leaving(i, j, lines, columns):
    if i == 0 or j == 0:
        return True
    if i == lines - 1 or j == columns - 1:
        return True 
    return False

def in_bounds(i, j, lines, columns):
    if i >= 0 and i < lines and j >= 0 and j < columns:
        return True
    return False

from collections import defaultdict

def in_loop(map, guard_i, guard_j):
    orientation = [(-1,0), (0,1), (1,0), (0,-1)]
    or_index = 0
    lines = len(map) 
    columns = len(map[0])
    tracker = defaultdict(list)

    while not guard_leaving(guard_i, guard_j, lines, columns):
            if or_index in tracker[(guard_i, guard_j)]:
                        return True
            tracker[(guard_i, guard_j)].append(or_index)
            next_i = guard_i + orientation[or_index][0]
            next_j = guard_j + orientation[or_index][1]
            if map[next_i][next_j] == "#":
                or_index += 1
                if or_index == 4:
                    or_index = 0 
            else:
                guard_i, guard_j = next_i, next_j
    return False       

with open('./input.txt') as f:
    map = []
    visited = set()
    for line in f:
        map.append(list(line.strip()))
    orientation = [(-1,0), (0,1), (1,0), (0,-1)]
    or_index = 0
    lines = len(map) 
    columns = len(map[0])
    guard_i, guard_j = 0, 0
    for i in range(lines):
        for j in range(columns):
            if map[i][j] == "^":
                print(f"Found it at {i}, {j}")
                guard_i, guard_j = i, j
                break
    cells = 1
    start_i, start_j = guard_i, guard_j
    visited.add((guard_i, guard_j))
    while not guard_leaving(guard_i, guard_j, lines, columns):
       next_i = guard_i + orientation[or_index][0]
       next_j = guard_j + orientation[or_index][1]
       # or_index = orientation index
       if (guard_i, guard_j) not in visited:
          cells += 1
          visited.add((guard_i, guard_j))
       if map[next_i][next_j] != "#":
           guard_i, guard_j = next_i, next_j
       else:
           or_index += 1
           if or_index == 4:
               or_index = 0
    possible_blockers = set()
    possible_blockers.add((guard_i, guard_j))
    for (i,j) in visited:
        possible_blockers.add((i,j))
        for (dir_i, dir_j) in orientation:
            if in_bounds(i + dir_i, j + dir_j, lines, columns):
                if map[i + dir_i][j + dir_j] != "#":
                    possible_blockers.add((i + dir_i, j + dir_j))
    possible_blockers.remove((start_i, start_j))
    loops = 0
    for (i, j) in possible_blockers:
        map[i][j] = "#"
        if in_loop(map, start_i, start_j):
            loops += 1
        map[i][j] = "."
    print(cells + 1)    
    print(loops)
   
