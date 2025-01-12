
def try_sign(goal, acc, numbers, index):
    if index == len(numbers):
        if acc == goal:
            return True
        return False
    if acc > goal:
        return False
    multiply = try_sign(goal, acc * numbers[index], numbers, index + 1)
    add = try_sign(goal, acc + numbers[index], numbers, index + 1)
    concat = try_sign(goal, acc * pow(10, len(str(numbers[index]))) + numbers[index], numbers, index + 1)
    return multiply or add or concat
    # try_sign(292, 11, [11, 6, 16, 20], 1)
    # try_sign(292, 66, [11, 6, 16, 20], 2)
    # try_sign(292, 1056, [11, 6, 16, 20], 3)
        # return False 
        # return try_sign(292, 66 + 16, [11, 6, 16, 20], 3)
        # try_sign(292, 82 * 20, 4) => 1640 return False 
        # try_sign(292, 82 + 20, 4) => return False 

with open('./input.txt') as f:
    correct = 0
    for line in f:
        line = line.strip()
        numbers = line.split(':')
        expected = int(numbers.pop(0))
        numbers = numbers[0].split(' ')
        numbers = [int(x) for x in numbers if x != '']
        acc = numbers[0]
        if try_sign(expected, acc, numbers, 1):
            correct += expected
    print(correct)
