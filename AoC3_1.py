import re

file = open('inputs/day3inp1')
inp = file.read()
file.close()

mul_list = re.findall("mul\(\d+,\d+\)", inp)

sum = 0
for operation in mul_list:
    nums = re.findall("\d+", operation)
    nums = [int(x) for x in nums]
    sum += nums[0] * nums[1]

print(sum)