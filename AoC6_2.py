from tqdm import tqdm
file = open('inputs/day6inp1')
rawinp = file.read().strip()
file.close()

rows = rawinp.split("\n")
matrix = []
for row in rows:
    matrix.append(list(row))

startpos = (0,0)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '^':
            startpos = (i,j)

dir_convertor = {
    'up': 0,
    'right': 1,
    'down': 2,
    'left': 3,
    0: 'up',
    1: 'right',
    2: 'down',
    3: 'left'
}

move_convertor = {
    'up': (-1,0),
    'right': (0,1),
    'down': (1,0),
    'left': (0,-1)
}


unique_positions = 0
vertices = set()
for i in tqdm(range(len(matrix))):
    for j in range(len(matrix[0])):
        facing_dir = 'up'
        pos = startpos
        if matrix[i][j] != '#' and matrix[i][j] != '^':
            matrix[i][j] = '#'
            vertices = set()
            while pos[0] < len(matrix) and pos[0] >= 0 and pos[1] < len(matrix[0]) and pos[1] >= 0:
                turn = True
                looping = False
                while(turn):
                    dest = tuple(map(lambda x, y: x+y, pos, move_convertor[facing_dir]))
                    # try:
                    if dest[0] < len(matrix) and dest[0] >= 0 and dest[1] < len(matrix[0]) and dest[1] >= 0:
                        if matrix[dest[0]][dest[1]] == '#':
                            facing_dir = dir_convertor[(dir_convertor[facing_dir] + 1) % 4]
                            if (pos, facing_dir) in vertices:
                                unique_positions += 1
                                looping = True
                                break
                            else:
                                vertices.add((pos, facing_dir))
                        else:
                            turn = False
                    else:
                        turn = False                  
                pos = dest
                if looping:
                    break
            matrix[i][j] = '.'

print(unique_positions)
with open('inputs/day6out1', 'w') as f:
    for row in matrix:
        for char in row:
            f.write(char)
        f.write('\n')