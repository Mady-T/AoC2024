import pandas as pd

inp = pd.read_csv('inputs/day1inp1', sep='\s+', header=None)

list1 = []
list2 = []
for row in inp[0]:
    list1.append(row)
for row in inp[1]:
    list2.append(row)

sim_score = 0

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            sim_score+=item1

print(sim_score)