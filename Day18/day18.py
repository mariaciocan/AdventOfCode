
def in_bounds(i, j, map):
    lines, columns = len(map), len(map[0])
    if i < 0 or i >= lines or j < 0 or j >= columns:
        return False
    return True 

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

import math
import heapq


with open("input-test.txt", "r") as input:
    grid_size = 71
    map = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    bytes = 0
    for line in input:
        x,y  = line.strip().split(',')
        map[int(x)][int(y)] = '#'
        bytes += 1
        if bytes == 1024:
            break
    visited = {}
    heap = [(0, 0, 0)]
    min_steps = math.inf
    while heap:
        curr_steps, x, y = heapq.heappop(heap)
        print(f"x, y {x}, {y}")
        if (x, y) in visited and visited[(x, y)] <= curr_steps:
            continue # skip this one 
        visited[(x, y)] = curr_steps
        if x == grid_size - 1 and y == grid_size - 1:
            if curr_steps < min_steps:
                min_steps = curr_steps
            continue
        if map[x][y] == '#':
            continue
        map[x][y] = 'O'
        for dx, dy in directions:
            if in_bounds(x + dx, y + dy, map):
                heapq.heappush(heap, (curr_steps + 1, x + dx, y + dy))
    print(min_steps)