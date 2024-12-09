from tqdm import tqdm

with open('inputs/day9inp1') as f:
    rawinp = f.read().strip()

diskspace = list()
fileid = 0

for i in range(len(rawinp)):
    if i%2 == 0:
        for j in range(int(rawinp[i])):
            diskspace.append(fileid)
        fileid+=1
    else:
        for j in range(int(rawinp[i])):
            diskspace.append('_')

last_pos = len(diskspace) - 1

i = last_pos
with tqdm(total = last_pos) as pbar:
    while i >= 0:
        if diskspace[i] != '_':
            size = 0
            id = diskspace[i]
            while diskspace[i-size] == id:
                size+=1
            i -= size - 1
            pbar.update(size-1)
            for j in range(i):
                flag = True
                for k in range(size):
                    if diskspace[j+k] != '_':
                        flag=False
                        break
                if flag:
                    for k in range(size):
                        diskspace[i+k], diskspace[j+k] = diskspace[j+k], diskspace[i+k]
                    break
        pbar.update(1)  
        i -= 1



checksum = 0
for i in range(len(diskspace)):
    if diskspace[i] != '_':
        checksum += i * diskspace[i]


print(checksum)
with open('inputs/day9out1', 'w') as f:
    f.write(str(diskspace))