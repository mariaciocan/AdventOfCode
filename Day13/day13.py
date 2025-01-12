


def greatest_common_divisor(x, y):
    if y == 0:
        return x
    return greatest_common_divisor(y, x % y)

def find_lcm(x, y):
    return (x / greatest_common_divisor(x, y)) * y

with open("input-test.txt") as input:
    questions = []
    current_question = []
    for line in input:
        print(line)
        if "Button A" in line or "Button B" in line:
            current_question.append(line.strip()[10:])
        elif "Prize" in line:
            current_question.append(line.strip()[7:])
        else:
            questions.append(current_question)
            current_question = []
    questions.append(current_question)
    cost = 0
    for question in questions:
        #print(question)
        coeff_a_x= int(question[0].split(',')[0][2:])
        coeff_a_y = int(question[0].split(',')[1][2:])
        coeff_b_x = int(question[1].split(',')[0][2:])
        coeff_b_y = int(question[1].split(',')[1][2:])
        target_x =  int(question[2].split(',')[0][2:]) + 10000000000000
        target_y =  int(question[2].split(',')[1][3:]) + 10000000000000
        scm = find_lcm(coeff_b_x, coeff_b_y)
        m1 = (scm / coeff_b_x)
        m2 = (scm / coeff_b_y)
        #print(f"multiply 1st with {m1}")
        #print(f"multiply 2nd with {m2}")
        na = ( target_x * m1 - target_y * m2 ) / (coeff_a_x * m1 - coeff_a_y * m2)
        if abs(round(na) - na) < 0.0001:
                nb = ( target_x - round(na) * coeff_a_x ) / coeff_b_x
                if abs(round(nb) - nb) < 0.0001:
                    cost += 3 * round(na) + round(nb)
    print(cost)