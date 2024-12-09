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
for i in range(len(diskspace)):
    if diskspace[i] == '_':
        try:
            while diskspace[last_pos] == '_':
                last_pos -= 1
            if last_pos < i:
                break
            diskspace[i], diskspace[last_pos] = diskspace[last_pos], diskspace[i]
        except IndexError:
            print(last_pos)
            break

checksum = 0
for i in range(len(diskspace)):
    if diskspace[i] != '_':
        checksum += i * diskspace[i]

print(checksum)
with open('inputs/day9out1', 'w') as f:
    f.write(str(diskspace))