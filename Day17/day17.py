from math import trunc

with open("input-test.txt", "r") as input:
    
    for line in input:
        if "Register A" in line:
            A = int(line.strip()[12:])
        elif "Register B" in line:
            B = int(line.strip()[12:])
        elif "Register C" in line:
            C = int(line.strip()[12:])
        elif "Program" in line:
            program = [int(x) for x in line.strip()[9:].split(',')]
    i = 0
    print(program)
    print(len(program))
    A = pow(2, 45) + 13
    print(f"A: {bin(A)}, B: {bin(B)}, C: {bin(C)}")
    output = []
    y = pow(2, 45)
    z = y * 2
    for A in range(y, z):
        current = []
        i = 0
        while i < len(program) - 1:
            operator = program[i]
            arg = program[i + 1]
            if arg == 4:
                arg = A
            elif arg == 5:
                arg = B
            elif arg == 6:
                arg = C
            if operator == 0: #adv
                A = trunc(A / pow(2, arg))
            elif operator == 1: #xor B and arg
                B = B ^ program[i + 1]
            elif operator == 2: #modulo 8
                B = arg % 8
            elif operator == 3:
                if A != 0:
                    i = program[i+1]
            elif operator == 4: # xor B and C
                B = B ^ C
            elif operator == 5:
                if str(arg % 8) != program[len(current)]:
                    i = 1000
                else:
                    current.append(str(arg % 8))
            elif operator == 6:
                B = trunc(A / pow(2, arg))
            elif operator == 7:
                C = trunc(A / pow(2, arg))
            if operator != 3 or (operator == 3 and A == 0):
                i += 2
        if len(current) == len(program):
            print(A)
            print(current)
            break
    print(','.join((output)))
    print(len(output))