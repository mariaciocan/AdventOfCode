



with open('./input-test.txt') as f:
    memory = ''
    for line in f:
        memory = line.strip()
    memory_list = []
    for char in memory:
        memory_list.append(int(char))
    index_file = len(memory_list) - 1
    index_empty = 1
    checksum = 0
    my_set = [(0, memory_list[0])]
    while index_empty <= index_file:
        mem_av = memory_list[index_empty]
        file_size = memory_list[index_file]
        id_file = index_file // 2
        if mem_av == 0:
            index_empty += 2
            idx = (index_empty - 1) // 2
            my_set.append((idx, memory_list[index_empty - 1]))
        elif file_size == 0:
            index_file -= 2
        else:
            if mem_av >= file_size:
                my_set.append((id_file, file_size))
                memory_list[index_empty] -= file_size
                index_file -= 2
            else:
                my_set.append((id_file, mem_av))
                memory_list[index_empty] = 0
                memory_list[index_file] -= mem_av

    index = 0
    for (id, times) in my_set:
        for j in range(index, index + times):
            checksum += id * j
        index += times
    print(checksum)

