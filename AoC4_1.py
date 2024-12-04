file = open('inputs/day4inp1')
rawinp = file.read()
file.close()

rows = rawinp.split("\n")
rows.pop() #remove trailing blank line
matrix = []
for row in rows:
    matrix.append(list(row))

def xmasDetector(arr): #checks for occurences of XMAS forwards and backwards
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
    candidates = [row[x:x+4] for x in range(len(row) - 4)]
    for candidate in candidates:
        if xmasDetector(candidate) == True:
            count+= 1
#vertical
for i in range(len(matrix)):
    col = [row[i] for row in matrix]
    candidates = [col[x:x+4] for x in range(len(col) - 4)]
    for candidate in candidates:
        if xmasDetector(candidate) == True:
            count+= 1

print(count)

