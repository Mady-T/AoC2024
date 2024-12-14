# Involves manual search with algorithmic shortlisting. Hit enter till you see a tree
import re

with open('inputs/day14inp1') as f:
    rawinp = f.read().strip()

rows = rawinp.split('\n')
positions = []
velocities = []
for row in rows:
    robot_attributes = row.split()
    pos = re.sub('p=','',robot_attributes[0])
    vel = re.sub('v=','',robot_attributes[1])
    positions.append([int(x) for x in pos.split(',')])
    velocities.append([int(x) for x in vel.split(',')])


def calcPosition(s, v, t, bounds):
    return ((s[0] + v[0]*t) % bounds[0], (s[1] + v[1]*t) % bounds[1])

def getQuadrant(pos, bounds):
    if pos[0] < bounds[0]//2 and pos[1] < bounds[1]//2:
        return 0
    elif pos[0] < bounds[0]//2 and pos[1] > bounds[1]//2:
        return 1
    elif pos[0] > bounds[0]//2 and pos[1] < bounds[1]//2:
        return 2
    elif pos[0] > bounds[0]//2 and pos[1] > bounds[1]//2:
        return 3
    else:
        return None

def printArea(positions, bounds):
    for i in range(bounds[1]):
        row = ''
        for j in range(bounds[0]):
            if (j, i) not in positions:
                row = row+'_'
            else:
                row = row+'*'
        print(row)

bounds = (101, 103)
j=0
while (True):
    final_pos = []
    num_middle = 0
    for i in range(len(positions)):
        fin_pos = calcPosition(positions[i], velocities[i], j, bounds)
        final_pos.append(fin_pos)
        if fin_pos[0] == bounds[0]//2:
            num_middle += 1
    if num_middle > 15:
        print(j)
        printArea(final_pos, bounds)
        input()
    print(num_middle)
    j+=1
