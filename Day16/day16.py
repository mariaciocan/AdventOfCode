import math
import heapq

def find_start_position(map):
    lines, columns = len(map), len(map[0])
    for i in range(lines):
        for j in range(columns):
            if map[i][j] == 'E':  # Start position
                return (i, j)

def in_bounds(map, i, j):
    lines, columns = len(map), len(map[0])
    return 0 <= i < lines and 0 <= j < columns

directions = {
    'E': (0, 1), 'O': (1, 0), 'W': (0, -1), 'N': (-1, 0)
}

# Possible turns from each direction
next_directions = {
    'E': ['O', 'N'], 'O': ['W', 'E'], 'W': ['N', 'O'], 'N': ['W', 'E']
}

with open("input-example.txt") as input:
    map = [list(line.strip()) for line in input]

    si, sj = find_start_position(map)

    heap = [(0, si, sj, 'E', 0, set())] 
    visited = {} 

    min_cost = math.inf
    optimal_paths = []      

while heap:
    curr_cost, si, sj, letter, steps, visited_cells = heapq.heappop(heap)

    if (si, sj, letter) in visited and visited[(si, sj, letter)] <= curr_cost:
        continue
    visited[(si, sj, letter)] = curr_cost  

    if map[si][sj] == 'S':  # end
        if curr_cost < min_cost:
            min_cost = curr_cost
            optimal_paths = [visited_cells]  
        elif curr_cost == min_cost:
            optimal_paths.append(visited_cells)
        continue

    if map[si][sj] == '#':
        continue

    new_visited_cells = visited_cells.copy()
    new_visited_cells.add((si, sj))

    for l in next_directions[letter]:
        if (si, sj, l) not in visited or visited[(si, sj, l)] > curr_cost + 1000:
            heapq.heappush(heap, (curr_cost + 1000, si, sj, l, steps + 1, new_visited_cells))

    dx, dy = directions[letter]
    if (si + dx, sj + dy, letter) not in visited or visited[(si + dx, sj + dy, letter)] > curr_cost + 1:
        heapq.heappush(heap, (curr_cost + 1, si + dx, sj + dy, letter, steps + 1, new_visited_cells))

all_unique_cells = set()

for path in optimal_paths:
    for i, j in path:
        map[i][j] = 'X'
    all_unique_cells.update(path)

print(f"Minimum cost: {min_cost}")
print(f"Number of unique cells in the optimal path(s): {len(all_unique_cells)}")

