from tqdm import tqdm

with open('inputs/day11inp1') as f:
    rawinp = f.read().strip()

stones = rawinp.split()

def getUpdateRule(stone):
    if stone == '0':
        return 1
    elif len(stone) % 2 == 0:
        return 2
    else:
        return 3
    
    
for blink in range(25):
    print("iter: " + str(blink) + ": " + str(len(stones)))
    stone_num = 0
    with tqdm(total = len(stones)) as pbar:
        while stone_num < len(stones):
            rule = getUpdateRule(stones[stone_num])
            old = stones.pop(stone_num)
            if rule == 1:
                stones.insert(stone_num, '1')
            elif rule == 2:
                part1 = str(int(old[:int(len(old)/2)]))
                part2 = str(int(old[int(len(old)/2):]))
                stones.insert(stone_num, part2)
                stones.insert(stone_num, part1)
                stone_num += 1
            elif rule == 3:
                stones.insert(stone_num, str(2024 * int(old)))
            stone_num += 1
            pbar.update(1)

# print(stones)
print(len(stones))