import re

file = open('inputs/day3inp1')
inp = file.read()
file.close()

mul_list = re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", inp)

sum = 0
enabled = True
for operation in mul_list:
    if operation == "do()":
        enabled = True
    elif operation == "don't()":
        enabled = False
    elif enabled:
        nums = re.findall("\d+", operation)
        nums = [int(x) for x in nums]
        sum += nums[0] * nums[1]

print(sum)