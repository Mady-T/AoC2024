import numpy as np

with open('inputs/day12inp1') as f:
    rawinp = f.read().strip()

rows = rawinp.split('\n')
matrix = list()
for row in rows:
    matrix.append(list(row))

garden = np.array(matrix)
checked = np.zeros_like(garden, dtype = 'bool')
bounds = garden.shape

def getAdjacents(indices):
    adjacents = list()
    if indices[0]+1 < bounds[0]:
        adjacents.append((indices[0]+1, indices[1]))
    if indices[1]+1 < bounds[1]:
        adjacents.append((indices[0], indices[1]+1))
    if indices[0]-1 >= 0:
        adjacents.append((indices[0]-1, indices[1]))
    if indices[1]-1 >= 0:
        adjacents.append((indices[0], indices[1]-1))
    return adjacents

def getRegion(indices, region_list = []):
    if not checked[indices]:
        region_list.append(indices)
        checked[indices] = True
        for coords in getAdjacents(indices):
            if not checked[coords]:
                if garden[indices] == garden[coords]:
                    getRegion(coords, region_list)
        return region_list
    else:
        return None

regions = []
for i in range(bounds[0]):
    for j in range(bounds[1]):
        if not checked[i,j]:
            regions.append(getRegion((i,j),[]))
            # print(str(i) + " " + str(j))
            
def getBoundaryCost(regions):
    area = 0
    perimeter = 0
    for coord1 in regions:
        area+=1
        perimeter += 4
        for coord2 in getAdjacents(coord1):
            if coord2 in regions:
                perimeter -= 1
    return area * perimeter

cost = 0
for region in regions:
    cost += getBoundaryCost(region)

print(cost)