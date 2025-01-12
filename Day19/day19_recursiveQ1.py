
from functools import cache

towels = set()

@cache
def is_possible(word):
    if word in towels:
        return True 
    for i in range(1, len(word)):
        if is_possible(word[:i]) and is_possible(word[i:]):
            return True
    return False

@cache
def count_ways(word):
    ways = 0
    if word == "":
        return 1
    for towel in towels:
        if word.startswith(towel):
            ways += count_ways(word[len(towel):])
    return ways


with open("input-test.txt", "r") as input:
    for line in input:
        if line == '\n':
            break
        elems = list(line.strip().split(', '))
        for elem in elems:
            towels.add(elem)
    designs = 0
    all_ways = 0
    for design in input:
        design = design.strip()
        if is_possible(design):
            designs += 1
            all_ways += count_ways(design)
            
    print(designs)
    print(all_ways)