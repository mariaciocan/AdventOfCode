import re 

with open('./input.txt') as f:
    data = f.read()
    total = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
    pairs = re.findall(pattern, data)
    disabled = False
    for p in pairs:
     if p == "don't()":
        disabled = True
     elif p == "do()":
        disabled = False
     else:
        to_remove = "mul()"
        x = ''.join([c for c in p if c not in to_remove])
        nums = x.split(',')
        if not disabled:
           total += int(nums[0]) * int(nums[1])
print(total)

