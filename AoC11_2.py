from tqdm import tqdm

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
    
class LList:
    def __init__(self):
        self.head = Node('header')
        self.length = 0

    def insertAfter(self, node, data):
        if node.next == None:
            node.next = Node(data)
        else:
            node.next = Node(data, node.next)
        self.length += 1
        return node.next
    
    def removeAfter(self, node):
        if node.next != None:
            data = node.next.data
            delnode = node.next
            node.next = node.next.next
            self.length -= 1
            del delnode
            return data
        else:
            return None

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

stones = LList()
current = stones.head

for stone in raw_stones:
    current = stones.insertAfter(current, stone)



for blink in range(75):
    print("iter: " + str(blink) + ": " + str(stones.length))
    prev = stones.head
    with tqdm(total = stones.length) as pbar:
        while True: #Exit at end of linkedlist
            current = prev.next
            old = stones.removeAfter(prev)
            if old == None:
                break
            rule = getUpdateRule(current.data)

            if rule == 1:
                current = stones.insertAfter(prev, '1')
            elif rule == 2:
                part1 = str(int(old[:int(len(old)/2)]))
                part2 = str(int(old[int(len(old)/2):]))
                current = stones.insertAfter(prev, part1)
                current = stones.insertAfter(current, part2)
            elif rule == 3:
                current = stones.insertAfter(prev, str(2024 * int(old)))
            prev = current
            # print(current.data)
            pbar.update(1)


current = stones.head
while current != None:
    print(current.data, end = " ")
    current = current.next
print()
print(stones.length)