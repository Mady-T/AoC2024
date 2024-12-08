import string

with open('inputs/day8inp1') as f:
    rawinp = f.read().strip()

rows = rawinp.split('\n')
matrix = list()
for row in rows:
    matrix.append(list(row))

antenna_types = list(string.ascii_letters + '0123456789')
zone_size = (len(matrix), len(matrix[0]))

def getAntinodes(antenna_locs, zone_size):
    antinodes = set()
    for loc1 in antenna_locs:
        for loc2 in antenna_locs:
            if loc1 != loc2:
                x_diff = loc2[0]-loc1[0] 
                y_diff = loc2[1]-loc1[1]
                if x_diff == 0:
                    for y in range(zone_size[1]):
                        antinodes.add((loc2[0], y))
                elif y_diff == 0:
                    for x in range(zone_size[0]):
                        antinodes.add((x, loc2[1]))
                else:
                    candidate_x = loc2[0]
                    candidate_y = loc2[1]
                    while candidate_x < zone_size[0] and candidate_x >= 0\
                    and candidate_y < zone_size[1] and candidate_y >= 0:
                        antinodes.add((candidate_x, candidate_y))
                        candidate_x += x_diff
                        candidate_y += y_diff
    return antinodes

antinode_set = set()
for antenna_type in antenna_types:
    antenna_locs = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == antenna_type:
                antenna_locs.append((i,j))
    antinode_set.update(getAntinodes(antenna_locs, zone_size))

print(len(antinode_set))
