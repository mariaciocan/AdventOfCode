def number_of_digits(x : int):
    digits = 0
    while x != 0:
        digits += 1
        x = x // 10
    return digits

from functools import cache

def expand_number(y : int):
    if y == 0:
        return [1]
    if number_of_digits(y) % 2 == 1:
        return [y * 2024]
    first_half = str(y)[:number_of_digits(y) // 2]
    second_half = str(y)[number_of_digits(y) // 2:]
    while second_half and second_half[0] == '0':
        second_half=second_half[1:]
    if second_half == '' or second_half == ' ':
        second_half = '0'
    return [int(first_half), int(second_half)]

@cache # game changer! 
def expand_n_times(x, times):
    if times == 0:
        return 1
    y = expand_number(x)
    if len(y) == 1:
        return expand_n_times(y[0], times - 1)
    return expand_n_times(y[0], times - 1 ) + expand_n_times(y[1], times - 1)
    



with open('./input.txt') as f:
    numbers = []
    from collections import defaultdict
    t = defaultdict(int)
    for line in f:
        numbers.extend([int(x) for x in line.strip().split(' ')])
    sumexp = 0
    for n in numbers:
        sumexp += expand_n_times(n, 75)
    print(sumexp)