with open('inputs/day10inp1') as f:
    rawinp = f.read().strip()

rows = rawinp.split('\n')
matrix = list()
for row in rows:
    matrow = []
    for char in row:
        matrow.append(int(char))
    matrix.append(matrow)

x_lim = len(matrix)-1
y_lim = len(matrix[0])-1

def traverse(map, elevation, xcoord, ycoord):
    if elevation != 9:
        peak_coords = set()
        if xcoord < x_lim and map[xcoord+1][ycoord] == elevation + 1:
            peak_coords.update(traverse(map, elevation+1, xcoord+1, ycoord))
        if xcoord > 0 and map[xcoord-1][ycoord] == elevation + 1:
            peak_coords.update(traverse(map, elevation+1, xcoord-1, ycoord))
        if ycoord < y_lim and map[xcoord][ycoord+1] == elevation + 1:
            peak_coords.update(traverse(map, elevation+1, xcoord, ycoord+1))
        if ycoord > 0 and map[xcoord][ycoord-1] == elevation + 1:
            peak_coords.update(traverse(map, elevation+1, xcoord, ycoord-1))
        # print(elevation)
        return peak_coords
    else:
        return {(xcoord, ycoord)}

sum_scores = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 0:
            peak_set = traverse(matrix, 0, i, j)
            print((peak_set))
            sum_scores += len(peak_set)

print(sum_scores)