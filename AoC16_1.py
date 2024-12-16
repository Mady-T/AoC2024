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
        # if numIters % 1 == 0:
        #     s = ''
        #     for row in costs:
        #         for num in row:
        #             if num == -np.inf:
        #                 s = s+'_____ '
        #             elif num == np.inf:
        #                 s = s+'##### '
        #             else:
        #                 s = s+str(int(num%100000)).zfill(5)+" "
        #         s += '\n'
        #     with open('inputs/day16out1', 'w') as f:
        #         f.write(s)



direction = np.array([0,1])
startpos, finishpos = getStartFinish(matrix)

traverse(startpos, direction, maze, costs)
print(costs[finishpos])

# best_cost = costs[finishpos]

# bestTiles = set()
# bestTiles.add(finishpos)


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
#     if tuple(pos) == finishpos:
#         if costs[tuple(down)] == m and tuple(down) not in bestTiles:
#             bestPath.append(down)
#             bestTiles.add(tuple(down))
#         if costs[tuple(left)] == m and tuple(left) not in bestTiles:
#             bestPath.append(left)
#             bestTiles.add(tuple(left))
#         continue
#     if (costs[tuple(down)] == m or costs[tuple(down)] == m + 1000 and costs[tuple(down+down-pos)] == m-1) and tuple(down) not in bestTiles:
#         bestPath.append(down)
#         bestTiles.add(tuple(down))
#     if (costs[tuple(up)] == m or costs[tuple(up)] == m + 1000 and costs[tuple(up+up-pos)] == m-1) and tuple(up) not in bestTiles:
#         bestPath.append(up)
#         bestTiles.add(tuple(up))
#     if (costs[tuple(left)] == m or costs[tuple(left)] == m + 1000 and costs[tuple(left+left-pos)] == m-1) and tuple(left) not in bestTiles:
#         bestPath.append(left)
#         bestTiles.add(tuple(left))
#     if (costs[tuple(right)] == m or costs[tuple(right)] == m + 1000 and costs[tuple(right+right-pos)] == m-1) and tuple(right) not in bestTiles:
#         bestPath.append(right)
#         bestTiles.add(tuple(right))

# print(len(bestTiles))
# print(bestTiles)
