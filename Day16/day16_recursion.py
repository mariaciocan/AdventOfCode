
import math 
def find_start_position(map):
    lines, columns = len(map), len(map[0])
    for i in range(lines):
        for j in range(columns):
            if map[i][j] == 'E':
                return (i, j)
            
def in_bounds(map, i, j):
     lines, columns = len(map), len(map[0])
     if i < 0 or i >= lines or j < 0 or j >= columns:
         return False
     return True

def traverse(map, i, j, score, visited, letter, turns):
    #print(f"At {i}, {j} orientation {letter} and visited {visited} and score {score}")
    directions = {}
    directions['E'] = (0,1) # facing east
    directions['O'] = (1,0) # facing south
    directions['W'] = (0,-1) # facing west
    directions['N'] = (-1,0) # facing north 
    next = {}
    next['E'] = ['O', 'N'] # turning 90 from east is either south(o) or north(n)
    next['O'] = ['W', 'E']
    next['W'] = ['N', 'O']
    next['N'] = ['W', 'E']
    if not in_bounds(map, i, j):
        print("Not in bounds")
        return math.inf
    if map[i][j] == 'S':
        print("Reached end")
        return score
    if map[i][j] == '#':
        print("Reached wall")
        return math.inf
    if (i, j) in visited:
        print("Already been here")
        return math.inf
    dx, dy = directions[letter]
    next_turn = next[letter]
    new_visited = visited.copy()
    new_visited.append((i, j))
    # Sadly this didn't work. 
    return min(traverse(map, i + dx, j + dy, score + 1, new_visited, letter),
                traverse(map, i + directions[next_turn[0]][0], j + directions[next_turn[0]][1], score + 1001, new_visited, next_turn[0]),
                traverse(map, i + directions[next_turn[1]][0], j + directions[next_turn[1]][1], score + 1001, new_visited, next_turn[1])
                )

with open("input-example.txt") as input:
    map = []
    for line in input:
        map.append(list(line.strip()))
    si, sj = find_start_position(map)
    v = []
    print(traverse(map, si, sj, 0, v, 'E', 0))
