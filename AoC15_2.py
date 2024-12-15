import re
import numpy as np

with open('inputs/day15inp1') as f:
    rawinp = f.read().strip()

inps = rawinp.split('\n\n')

warehouse = []
for row in inps[0].split('\n'):
    subbed = re.sub('#','##', re.sub('O', '[]', re.sub('@', '@.', re.sub('\.', '..', row))))
    warehouse.append(list(subbed))

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
    
def testMove(pos, dir, grid, symbol):
    dirVect = getDirVector(dir)
    newPos = np.add(pos,dirVect)
    newSymb = grid[tuple(newPos)]
    if newSymb == '#':
        return [None, None]
    elif newSymb == '[' or newSymb == ']':
        if newSymb == '[':
            nextPosMain = testMove(newPos, dir, grid, newSymb)
            nextPosSide = testMove(np.add(newPos, [0,1]), dir, grid, ']')
            if nextPosMain[0] == None or nextPosSide[0] == None:
                return [None, None]
        elif newSymb == ']':
            nextPosMain = testMove(newPos, dir, grid, newSymb)
            nextPosSide = testMove(np.add(newPos, [0,-1]), dir, grid, '[')
            if nextPosMain[0] == None or nextPosSide[0] == None:
                return [None, None]
    return newPos


def makeMove(pos, dir, grid, symbol = '@'):
    dirVect = getDirVector(dir)
    newPos = np.add(pos,dirVect)
    newSymb = grid[tuple(newPos)]
    if newSymb == '#':
        return [None, None]
    elif newSymb == '[' or newSymb == ']':
        if dir == '>' or dir == '<':
            nextPos = makeMove(newPos, dir, grid, newSymb)
            if nextPos[0] == None:
                return [None, None]
            else:
                grid[tuple(newPos)] = symbol
                grid[tuple(pos)] = '.'
        else:
            if newSymb == '[':
                nextPosMain = testMove(newPos, dir, grid, newSymb)
                nextPosSide = testMove(np.add(newPos, [0,1]), dir, grid, ']')
                if nextPosMain[0] == None or nextPosSide[0] == None:
                    return [None, None]
                else:
                    makeMove(newPos, dir, grid, newSymb)
                    makeMove(np.add(newPos, [0,1]), dir, grid, ']')
                    grid[tuple(newPos)] = symbol
                    grid[tuple(pos)] = '.'
            elif newSymb == ']':
                nextPosMain = testMove(newPos, dir, grid, newSymb)
                nextPosSide = testMove(np.add(newPos, [0,-1]), dir, grid, '[')
                if nextPosMain[0] == None or nextPosSide[0] == None:
                    return [None, None]
                else:
                    makeMove(newPos, dir, grid, newSymb)
                    makeMove(np.add(newPos, [0,-1]), dir, grid, '[')
                    grid[tuple(newPos)] = symbol
                    grid[tuple(pos)] = '.'

    else:
        grid[tuple(newPos)] = symbol
        grid[tuple(pos)] = '.'
    return newPos

def getTotalGpsCoords(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '[':
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

# print(warehouse)
print(getTotalGpsCoords(warehouse))