import numpy as np
from collections import deque

with open('inputs/day16testinp.txt') as f:
    rawinp = f.read().strip()

rows = rawinp.split('\n')
matrix = list()
for row in rows:
    matrix.append(list(row))

maze = np.array(matrix)
costs = np.ones_like(maze, dtype = int) * np.inf

def getStartFinish(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                start = (i, j)
            if matrix[i][j] == 'E':
                finish = (i, j)
    return start, finish

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
    
CWMATRIX = np.array([[0, -1], [1, 0]])
CCWMATRIX = np.array([[0, 1], [-1, 0]])

def traverse(startPos, startDir, maze, costs):
    heuristic = 0
    costs[tuple(startPos)] = 0
    posStack = deque([(startPos, startDir, heuristic)])
    numIters = 0
    while len(posStack) > 0:
        popped = posStack.popleft()
        pos, orientation, heuristic = popped[0], popped[1], popped[2]
        # print(pos, orientation, heuristic)
        if maze[tuple(pos)] == '#':
            costs[tuple(pos)] = np.inf
            continue
        else:
            if maze[tuple(pos)] == 'E':
                costs[tuple(pos)] = heuristic
                # print(heuristic)
                continue
            else:
                fwd = pos + orientation
                cw = pos + (orientation @ CWMATRIX)
                ccw = pos + (orientation @ CCWMATRIX)
                if costs[tuple(fwd)] > heuristic+1: # traverse(fwd, orientation, heuristic+1, maze, costs):
                    costs[tuple(fwd)] = heuristic+1
                    posStack.append((fwd, orientation, heuristic+1))
                if costs[tuple(cw)] > heuristic+1001: # traverse(cw, orientation @ CWMATRIX, heuristic+1001, maze, costs):
                    costs[tuple(cw)] = heuristic+1001
                    posStack.append((cw, orientation @ CWMATRIX, heuristic+1001))
                if costs[tuple(ccw)] > heuristic+1001: # traverse(ccw, orientation @ CCWMATRIX, heuristic+1001, maze, costs):
                    costs[tuple(ccw)] = heuristic+1001
                    posStack.append((ccw, orientation @ CCWMATRIX, heuristic+1001))
        # numIters += 1
        # if numIters % 100000 == 0:
        #     print(len(posStack))
        #     mat = []
        #     for row in costs:
        #         s = ''
        #         for num in row:
        #             if num == -np.inf:
        #                 s = s+'_'
        #             elif num == np.inf:
        #                 s = s+'#'
        #             else:
        #                 s = s+str(num%10)
        #         mat.append(s)
        #     with open('inputs/day16out1', 'w') as f:
        #         f.write(str(mat))



direction = np.array([0,1])
startpos, finishpos = getStartFinish(matrix)

traverse(startpos, direction, maze, costs)
print(costs[finishpos])

bestTiles = set(finishpos)

# bestPath = deque([np.array(finishpos)])
# while len(bestPath)>0:
#     pos = bestPath.pop()
#     if (pos == np.array(startpos)).all():
#         continue
#     up = pos + np.array([-1,0])
#     down = pos + np.array([1,0])
#     left = pos + np.array([0,-1])
#     right = pos + np.array([0,1])
#     m = min(costs[tuple(down)], costs[tuple(up)], costs[tuple(right)], costs[tuple(left)])
#     if costs[tuple(down)] == m:
#         bestPath.append(down)
#         bestTiles.add(tuple(down))
#     if costs[tuple(up)] == m:
#         bestPath.append(up)
#         bestTiles.add(tuple(up))
#     if costs[tuple(left)] == m:
#         bestPath.append(left)
#         bestTiles.add(tuple(left))
#     if costs[tuple(right)] == m:
#         bestPath.append(right)
#         bestTiles.add(tuple(right))

# print(len(bestTiles))

# mat = np.zeros_like(costs, dtype = int)
# for tile in bestTiles:
#     mat[tile] = 1

# print(mat)

# with open('inputs/day16out1', 'w') as f:
#     out = [str(x) + '\n' for x in mat]
#     f.write(str(out))