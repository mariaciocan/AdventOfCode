

def in_bounds(i, j, map):
    lines = len(map)
    columns = len(map[0])
    if i < 0 or i >= lines or j < 0 or j >= columns:
        return False
    return True

with open('./input.txt') as f:
    map = []
    for line in f:
        map.append([int(x) for x in line.strip().split(' ')])
    directions = [(1,0), (0,1), (-1, 0), (0, -1)]
    total_sum = 0
    total_trails = 0
    lines, columns = len(map), len(map[0])
    for i in range(lines):
        for j in range(columns):
            if map[i][j] == 0: # trailhead
                trail_sum = 0
                trails = 0
                queue = []
                nines = set()
                for dir_i, dir_j in directions:
                    if in_bounds(i + dir_i, j + dir_j, map) and map[i + dir_i][j + dir_j] == 1:
                        queue.append((i + dir_i, j + dir_j, 1))
                while queue:
                    curr_i, curr_j, curr_h = queue.pop()
                    if curr_h == 9:
                        nines.add((curr_i, curr_j))
                        trail_sum += 1
                    else:
                        for dir_i, dir_j in directions:
                            if in_bounds(curr_i + dir_i, curr_j + dir_j, map) and map[curr_i + dir_i][curr_j + dir_j] == curr_h + 1:
                                queue.append((curr_i + dir_i, curr_j + dir_j, curr_h + 1))
                total_sum += len(nines)
                total_trails += trail_sum
    print(total_sum)
    print(total_trails)
