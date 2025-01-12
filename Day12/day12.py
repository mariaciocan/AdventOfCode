
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
map = []


def in_bounds(i, j, lines, columns):
    if i < 0 or i >= lines or j < 0 or j >= columns:
            return False
    return True

def count_foreign_neighbours(i, j):
    fnn = [] # foreign neighbours (not from the same fence)
    lines = len(map)
    columns = len(map[0])
    for dx, dy in directions:
        if not in_bounds(i + dx, j + dy, lines, columns):
              fnn.append((dx, dy))
        elif map[i + dx][j + dy] != map[i][j]:
              fnn.append((dx, dy))
    return fnn


with open("input-test.txt") as input:
   
    for line in input:
            map.append(line.strip())
    regions = []
    lines = len(map)
    columns = len(map[0])
    visited = set()
    for i in range(lines):
          for j in range(columns):
                if (i, j) not in visited:
                      letter = map[i][j]
                      traverse = [(i , j)]
                      region = []
                      while traverse:
                            x, y = traverse.pop()
                            region.append((x, y))
                            visited.add((x,y))
                            for dx, dy in directions:
                                  if in_bounds(x+dx, y+dy, lines, columns) and map[x+dx][y+dy] == letter and (x+dx, y+dy) not in visited:
                                        traverse.append((x+dx, y+dy))
                                        visited.add((x + dx,y + dy))
                      regions.append((letter, region))
    fence = 0
    fence_q2 = 0
    for region in regions:
          perimeter = 0
          edges = 0
          for x,y in region[1]:
                letter = map[x][y]
                fn = count_foreign_neighbours(x, y)
                perimeter += len(fn)
                for dx, dy in fn:
                      if dx != 0:
                            if not in_bounds(x, y - 1, lines, columns):
                                  edges += 1
                            elif map[x][y - 1] != letter:
                                  edges += 1
                            elif map[x][y - 1] == letter and (dx, dy) not in count_foreign_neighbours(x, y - 1):
                                  edges += 1
                      else:
                            if dy != 0:
                                  if not in_bounds(x - 1, y, lines, columns):
                                        edges += 1
                                  elif map[x-1][y] != letter:
                                        edges += 1
                                  elif map[x-1][y] == letter and (dx, dy) not in count_foreign_neighbours(x - 1, y):
                                        edges += 1
          fence += perimeter * len(region[1])
          fence_q2 += len(region[1]) * edges
    print(fence)
    print(fence_q2) # Question 2 



