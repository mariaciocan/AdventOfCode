
with open("input.txt") as input:
    robots = []
    for line in input:
        pos, vec = line.strip().split(' ')
        pos, vec = pos[2:], vec[2:]
        pos_x, pos_y = int(pos.split(',')[0]), int(pos.split(',')[1])
        vec_x, vec_y = int(vec.split(',')[0]), int(vec.split(',')[1])
        robots.append([(pos_x, pos_y), (vec_x, vec_y)])
    xtiles, ytiles = 101, 103
    min_danger = None
    res_second = 0
    pic = []
    for second in range(101*103 + 1):
        q1, q2, q3, q4 = 0, 0, 0, 0
        final_robots = []
        for robot in robots:
            pos_x, pos_y = robot[0][0], robot[0][1]
            vec_x, vec_y = robot[1][0], robot[1][1]
            x = (pos_x + second * vec_x) % xtiles
            y = (pos_y + second * vec_y) % ytiles
            if x < 50 and y < 51:
                q1 += 1
            elif x < 50 and y > 51:
                q2 += 1
            elif x > 50 and y < 51:
                q3 += 1
            elif x > 50 and y > 51:
                q4 += 1
            final_robots.append((x, y))
        if not min_danger or q1 * q2 * q3 * q4 < min_danger:
            min_danger = q1*q2*q3*q4
            res_second = second
            pic = final_robots
    print(res_second)
    matrix = [['.' for _ in range(xtiles)] for _ in range(ytiles)]
    for i, j in pic:
        matrix[j][i] = '*'
    output = open('./christmas-tree.txt', 'w')
    for line in matrix:
        output.write(str(line))
        output.write('\n')
    output.close()
