def find_left_empty(disk, target):
    for i in range(len(disk)):
        if disk[i] != '.':
            continue
        start = i
        while i < len(disk) and disk[i] == '.':
            i = i + 1
        end = i
        if (end - start) >= target:
            return (start, end)
    return (-1, -1)

def remove(disk, value):
    for i in range(len(disk)):
        if disk[i] == value:
            disk[i] = '.'
    return disk

with open('./input.txt') as f:
    memory = ''
    for line in f:
        memory = [int(x) for x in line.strip()]
    disk = []
    sizes = [0 for i in range(len(memory) // 2 + 1)]
    for i in range(len(memory)):
        if i % 2 == 0:
            sizes[i // 2] = memory[i]
            for j in range(memory[i]):
                disk.append(i // 2)
        else:
            for j in range(memory[i]):
                disk.append('.')
    file_id = len(sizes) - 1
    while file_id > 0:
        target = sizes[file_id]
        start, end = find_left_empty(disk, target)
        if start != -1 and end != -1 and start < disk.index(file_id):
            disk = remove(disk, file_id)
            for j in range(start, start + target):
                disk[j] = file_id
        file_id -= 1
    checksum = 0
    for i in range(len(disk)):
        if disk[i] != '.':
            checksum += disk[i] * i 
    print(checksum)




    