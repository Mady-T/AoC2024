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

def getDiagonals(prime_index, sec_index):
    out_of_bounds_index = (2*sec_index[0] - prime_index[0], 2*sec_index[1] - prime_index[1])
    diagonals = getAdjacents(sec_index)
    if out_of_bounds_index in diagonals:
        diagonals.remove(out_of_bounds_index)
    diagonals.remove(prime_index)
    return diagonals

def printGarden(regions, fill = 1):
    arr = np.zeros(garden.shape, dtype = int)
    for region in regions:
        arr[region] = fill
    arr = arr.tolist()
    for row in arr:
        print(row)
    print()
            
def getBoundaryCost(regions):
    # region_set = set(regions)
    area = 0
    perimeter = 0
    region_set= set()
    for coord in regions:
        area += 1
        if coord not in region_set:
            region_set.add(coord)
            adjs = list(set(getAdjacents(coord)) & region_set)
            if len(adjs) == 0:
                perimeter += 4
            elif len(adjs) == 1:
                num_diags = len(set(getDiagonals(coord, adjs[0])) & region_set)
                if num_diags == 0:
                    perimeter += 0
                elif num_diags == 1:
                    perimeter += 2
                elif num_diags == 2:
                    perimeter += 4
            elif len(adjs) == 2:
                diag1 = set(getDiagonals(coord, adjs[0])) & region_set
                diag2 = set(getDiagonals(coord, adjs[1])) & region_set
                if max(list(np.subtract(adjs[0], adjs[1]))) < 2:
                    if len(diag1) == 2 and len(diag2) == 2:
                        perimeter+=2
                    elif len(diag1) == 0 and len(diag2) == 0:
                        perimeter-=2
                    elif len(diag1) == 1 and len(diag2) == 1:
                        if len(diag1 & diag2) == 1:
                            perimeter -= 2
                        else:
                            perimeter += 0
                    else:
                        perimeter += 0
                else:
                    perimeter += -4 + 2*(len(diag1 | diag2))
            elif len(adjs) == 3:
                non_region = list(set(getAdjacents(coord)) - set(adjs))
                if len(non_region) > 0:
                    diags = set(getDiagonals(coord, non_region[0])) & region_set
                    perimeter += -4 + 2*(len(diags))
                else:
                    perimeter -= 4
            else:
                perimeter -= 4
            # print(perimeter)
            # printGarden(region_set)
    return (area, perimeter)

cost = 0
for region in regions:
    cost_incr = getBoundaryCost(region)
    print(str(garden[region[0]])+": "+str(cost_incr))
    cost+= cost_incr[0]*cost_incr[1]

print(cost)

# cost_incr = getBoundaryCost(regions[0])

