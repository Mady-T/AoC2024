file = open('inputs\day4inp1')
rawinp = file.read().strip()
file.close()

rows = rawinp.split("\n")
# rows.pop() #remove trailing blank line
matrix = []
for row in rows:
    matrix.append(list(row))
MAXLEN = len(matrix) - 1

def masDetector(arr, locx, locy): #checks for occurences of XMAS forwards and backwards
    flag1 = False
    flag2 = False
    if locx < 1 or locx >= MAXLEN or locy < 1 or locy >= MAXLEN:
        return False
    try:
        if (arr[locx-1][locy-1] == 'M' and arr[locx+1][locy+1] == 'S') or \
            (arr[locx-1][locy-1] == 'S' and arr[locx+1][locy+1] == 'M'):
            flag1 = True
        if (arr[locx-1][locy+1] == 'M' and arr[locx+1][locy-1] == 'S') or \
            (arr[locx-1][locy+1] == 'S' and arr[locx+1][locy-1] == 'M'):
            flag2 = True
    except IndexError:
        print("index exception")
        pass
    if flag1 and flag2:
        return True
    else:
        return False

# PREREQUISITE: number of rows == number of columns
count = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 'A':
            if masDetector(matrix, i, j):
                count+=1


print(count)