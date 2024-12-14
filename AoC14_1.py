import re
from collections import Counter

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

bounds = (101, 103)
final_pos = []
quads = []
for i in range(len(positions)):
    fin_pos = calcPosition(positions[i], velocities[i], 100, bounds)
    final_pos.append(fin_pos)
    quads.append(getQuadrant(fin_pos, bounds))
quad_counts = Counter(quads)    

print(quad_counts[0] * quad_counts[1] * quad_counts[2] * quad_counts[3])
