with open('inputs/day11inp1') as f:
    rawinp = f.read().strip()

raw_stones = rawinp.split()

def getUpdateRule(stone):
    if stone == '0':
        return 1
    elif len(stone) % 2 == 0:
        return 2
    else:
        return 3
    
stone_ref = dict()
    
def getNumStones(stone, blink_num, total_blinks):
    if blink_num != total_blinks:
        if (stone, blink_num) not in stone_ref.keys():
            rule = getUpdateRule(stone)
            if rule == 1:
                num_stones = getNumStones('1', blink_num + 1, total_blinks)
            elif rule == 2:
                num_stones = getNumStones(str(int(stone[:int(len(stone)/2)])), blink_num+1, total_blinks)
                num_stones += getNumStones(str(int(stone[int(len(stone)/2):])), blink_num+1, total_blinks)
            elif rule == 3:
                num_stones = getNumStones(str(int(stone)*2024), blink_num+1, total_blinks)
            stone_ref[(stone, blink_num)] = num_stones
        else:
            num_stones = stone_ref[(stone, blink_num)]
        return num_stones
    else:
        return 1

total_stones = 0  
for stone in raw_stones:
    total_stones += getNumStones(stone, 0, 75)

print(total_stones)