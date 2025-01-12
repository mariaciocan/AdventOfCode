
with open("input.txt") as input:
    robots = []
    for line in input:
        pos, vec = line.strip().split(' ')
        pos, vec = pos[2:], vec[2:]
        pos_x, pos_y = int(pos.split(',')[0]), int(pos.split(',')[1])
        vec_x, vec_y = int(vec.split(',')[0]), int(vec.split(',')[1])

        robots.append([(pos_x, pos_y), (vec_x, vec_y)])
    xtiles, ytiles = 101, 103
    final_robots = []
    for robot in robots:
        pos_x, pos_y = robot[0][0], robot[0][1]
        vec_x, vec_y = robot[1][0], robot[1][1]
        x = (pos_x + 100 * vec_x) % xtiles
        y = (pos_y + 100 * vec_y) % ytiles
        final_robots.append((x, y))
    overall = 1
    quadrant = 0
    for x,y in final_robots:
        if x < 50 and y < 51:
            quadrant += 1
    overall *= quadrant

    quadrant = 0
    for x,y in final_robots:
        if x < 50 and y > 51:
            quadrant += 1

    overall *= quadrant
    quadrant = 0
    for x,y in final_robots:
        if x > 50 and y < 51:
            quadrant += 1
    overall *= quadrant

    quadrant = 0
    for x,y in final_robots:
        if x > 50 and y > 51:
            quadrant += 1
    overall *= quadrant

    print(overall)