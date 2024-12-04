file = open('inputs/day4inp1')
rawinp = file.read()
file.close()

rows = rawinp.split("\n")
rows.pop() #remove trailing blank line
matrix = []
for row in rows:
    matrix.append(list(row))

def xmasDetector(arr): #checks for occurences of XMAS forwards and backwards
    if len(arr) < 4:
        return False
    if arr[0] == 'X' and arr[1] == 'M' and arr[2] == 'A' and arr[3] =='S':
        return True
    elif arr[3] == 'X' and arr[2] == 'M' and arr[1] == 'A' and arr[0] =='S':
        return True
    else:
        return False

count = 0
#PREREQUISITE: number of rows == number of columns
#horizontal
for row in matrix:
    candidates = [row[x:x+4] for x in range(len(row) - 3)]
    for candidate in candidates:
        if xmasDetector(candidate) == True:
            count+= 1
#vertical
for i in range(len(matrix)):
    col = [row[i] for row in matrix]
    candidates = [col[x:x+4] for x in range(len(col) - 3)]
    for candidate in candidates:
        if xmasDetector(candidate) == True:
            count+= 1
#diagonals
MATLEN = len(matrix) - 1
for rank in range(len(matrix)):
    diag1 = []
    diag2 = []
    diag3 = []
    diag4 = []
    for j in range(rank + 1):
        diag1.append(matrix[j][rank-j])
        if rank != MATLEN:
            diag2.append(matrix[MATLEN-j][MATLEN-rank+j])
        diag3.append(matrix[j][MATLEN-rank+j])
        if rank != MATLEN:
            diag4.append(matrix[MATLEN-j][rank-j])
    candidates = []
    candidates.append([diag1[x:x+4] for x in range(len(diag1) - 3)])
    candidates.append([diag2[x:x+4] for x in range(len(diag2) - 3)])
    candidates.append([diag3[x:x+4] for x in range(len(diag3) - 3)])
    candidates.append([diag4[x:x+4] for x in range(len(diag4) - 3)])
    for diagonal_type in candidates:
        # print(diagonal_type)
        for candidate in diagonal_type:
            if xmasDetector(candidate) == True:
                count+= 1


print(count)

