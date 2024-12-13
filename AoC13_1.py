import numpy as np
import re

with open('inputs/day13inp1') as f:
    rawinp = f.read().strip()

A_button = re.findall('Button A: .*', rawinp)
B_button = re.findall('Button B: .*', rawinp)
Prize = re.findall('Prize: .*', rawinp)

A_increments = []
B_increments = []
prize_locs = []
for i in range(len(A_button)):
    A_incr = re.sub(' Y\+', '', re.sub('X\+', '', re.sub('Button A: ', '', A_button[i]))).strip()
    A_increments.append([int(x) for x in A_incr.split(',')])
    B_incr = re.sub(' Y\+', '', re.sub('X\+', '', re.sub('Button B: ', '', B_button[i]))).strip()
    B_increments.append([int(x) for x in B_incr.split(',')])
    p_loc = re.sub(' Y=', '', re.sub('X=', '', re.sub('Prize: ', '', Prize[i]))).strip()
    prize_locs.append([int(x) for x in p_loc.split(',')])

print(prize_locs)
