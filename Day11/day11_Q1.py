from collections import defaultdict


def number_of_digits(x: int):
    digits = 0
    while x != 0:
        digits += 1
        x //= 10
    return digits

with open('./input-test.txt') as file:
    numbers = []
    for line in file:
        numbers.extend([int(x) for x in line.strip().split(' ')])
    new_numbers = []
    for _ in range(3):
        for n in numbers:
            if n == 0:
                new_numbers.append(1)
                continue
            if number_of_digits(n) % 2 == 0:
                first_half = str(n)[:number_of_digits(n) // 2]
                second_half = str(n)[number_of_digits(n) // 2:]
                while second_half and second_half[0] == '0':
                    second_half = second_half[1:]
                if second_half == '':
                    second_half = '0'
                new_numbers.append(int(first_half))
                new_numbers.append(int(second_half))
            else:
                new_numbers.append(n * 2024)
        numbers = new_numbers
        new_numbers = []
       
    print(len(numbers))