import re
import numpy as np

with open('inputs/day15inp1') as f:
    rawinp = f.read().strip()

inps = rawinp.split('\n\n')

warehouse = []
for row in inps[0].split('\n'):
    warehouse.append(list(row))

warehouse = np.array(warehouse)
# print(warehouse)

dirs = re.sub('\n', '', inps[1])

def getRobotPos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return np.array([i, j])
    return None

def getDirVector(dir):
    if dir == '^':
        return np.array([-1,0])
    elif dir == 'v':
        return np.array([1,0])
    elif dir == '>':
        return np.array([0,1])
    elif dir == '<':
        return np.array([0,-1])
    else:
        return None

def makeMove(pos, dir, grid, symbol = '@'):
    dirVect = getDirVector(dir)
    newPos = np.add(pos,dirVect)
    if grid[tuple(newPos)] == '#':
        return [None, None]
    elif grid[tuple(newPos)] == 'O':
        nextPos = makeMove(pos+dirVect, dir, grid, 'O')
        if nextPos[0] == None:
            return [None, None]
        else:
            grid[tuple(newPos)] = symbol
            grid[tuple(pos)] = '.'
    else:
        grid[tuple(newPos)] = symbol
        grid[tuple(pos)] = '.'
    # try:
    #     grid[tuple(newPos)],  grid[tuple(pos)] = grid[tuple(pos)], grid[tuple(newPos)]
    # except ValueError:
    #     print(tuple(newPos))
    #     exit()
    return newPos

def getTotalGpsCoords(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                total += i*100 + j
    return total

robotPos = getRobotPos(warehouse)

for step in dirs:
    newPos = makeMove(robotPos, step, warehouse)
    if newPos[0] != None:
        robotPos = newPos
    # print(step)
    # print(warehouse)
    # input()
print(getTotalGpsCoords(warehouse))