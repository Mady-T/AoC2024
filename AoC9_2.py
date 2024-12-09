from tqdm import tqdm

with open('inputs/day9inp1') as f:
    rawinp = f.read().strip()

diskspace = []
fileid = 0

for i in range(len(rawinp)):
    if i%2 == 0:
        diskspace.append((fileid, int(rawinp[i])))
        fileid+=1
    else:
        diskspace.append(('_', int(rawinp[i])))

for i in tqdm(range(len(diskspace) - 1, 0, -1)):
    if diskspace[i][0] != '_':
        j = 0
        space_req = diskspace[i][1]
        while j < i:
            if space_req <= diskspace[j][1] and diskspace[j][0] == '_':
                space_left = diskspace[j][1] - space_req
                file = diskspace[i]
                diskspace.insert(j, (diskspace.pop(j)[0], space_left))
                diskspace.insert(j, file)
                diskspace.pop(i+1)
                break
            j+=1

with open('inputs/day9out2', 'w') as f:
    f.write(str(diskspace))
                
index = 0
checksum = 0
for i in tqdm(range(len(diskspace))):
    if diskspace[i][0] != '_':
        for j in range(diskspace[i][1]):
            checksum += diskspace[i][0] * index
            index += 1
    else:
        index += diskspace[i][1]

print(index)
print(checksum)
                

