

# Issue with this is that always picking the longest max can prevent you from finding a solution. 
# Example [ab, abx, xr] and target = "abxr", if you pick abx than you can't match r 


with open("input-test.txt", "r") as input:
    towels = set()
    for line in input:
        if line == '\n':
            break
        elems = list(line.strip().split(', '))
        for elem in elems:
            towels.add(elem)
    print(towels)
    output = open("output.txt", "w")
    designs = 0
    for design in input:
        if design == '\n':
            break
        design = design.strip()
        print(f"Checking design: {design}\n")
        possible = True
        index = 0
        while possible and index < len(design):
            max_att = len(design) - index
            found = False
            while max_att > 0 and not found:
                if str(design[index:index + max_att]) in towels:
                    print(f"Found {str(design[index:index + max_att])} and now max_att : {max_att}")
                    found = True
                else:
                    max_att -= 1
            if not found:
                possible = False
            else:
                index += max_att
        if possible:
            #print(f"Design {design} is possible")
            designs += 1
    print(designs)