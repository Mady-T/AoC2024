import numpy as np
import re
from scipy.optimize import linprog

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
    prize_locs.append([int(x)+10000000000000 for x in p_loc.split(',')])

adjusted_prizes = []
totalCost = 0
for i in range(len(prize_locs)):
    cost = 0
    A_x, A_y = A_increments[i][0], A_increments[i][1]
    B_x, B_y = B_increments[i][0], B_increments[i][1]
    P_x, P_y = prize_locs[i][0], prize_locs[i][1]
    coeffs = np.array([[A_x, B_x],[A_y, B_y]])
    consts = np.array([P_x, P_y]).transpose()
    objective = np.array([3,1])
    result = linprog(objective, A_eq=coeffs, b_eq=consts, integrality=1, options={'presolve': False})
    if result.status == 0:
        cost += result.fun
    elif result.status != 2:
        print('unforseen')
    totalCost += cost
print(totalCost)

