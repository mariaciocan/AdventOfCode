def signOf(number):
    if number < 0: 
        return '-'
    return '+'

def is_safe_level(line_nums):
   prev_diff = None
   for i in range(len(line_nums) - 1):
       number = int(line_nums[i])
       next_number = int(line_nums[i+1])
       diff = (next_number - number)
       if 0 == abs(diff) or 3 < abs(diff):
           attempt1 = line_nums[:i] + line_nums[i+1:]
           if is_safe_level(attempt1):
               return True
           attempt2 =  line_nums[:i+1] + line_nums[i+2:]
           if is_safe_level(attempt2):
               return True
           return False 
       if prev_diff:
            if signOf(diff) is not signOf(prev_diff):
                attempt1 = line_nums[:i] + line_nums[i+1:]
                if is_safe_level(attempt1):
                    return True
                attempt2 =  line_nums[:i+1] + line_nums[i+2:]
                if is_safe_level(attempt2):
                    return True
            return False
       prev_diff = diff
   
   return True


with open('./input-test.txt') as f:
    data = f.read()
    data = data.split('\n')
    safe_reports = 0
    for line in data:
        diff = None
        line_nums = line.split(' ')
        if is_safe_level(line_nums):
            safe_reports += 1

    print(safe_reports)
        


