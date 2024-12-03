import pandas as pd

inp = pd.read_csv('inputs/day1inp1', sep='\s+', header=None)

list1 = []
list2 = []
for row in inp[0]:
    list1.append(row)
for row in inp[1]:
    list2.append(row)

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)
