import re

with open('inputs/day5inp1') as f:
    rawinp = f.read().strip()

rule_list = re.findall('\d+\|\d+', rawinp)
rules = []
for rule in rule_list:
    rule = rule.split('|')
    rules.append((int(rule[0]), int(rule[1])))
rawinp = re.sub('\d+\|\d+', '', rawinp)
rawinp = rawinp.strip()
update_list = rawinp.split('\n')
updates = []
for update in update_list:
    upd = update.split(',')
    for i in range(len(upd)):
        upd[i] = int(upd[i])
    updates.append(upd)


def checkRules(index, update, rules):
    for rule in rules:
        if update[index] == rule[1]:
            for i in range(index+1, len(update)):
                if update[i] == rule[0]:
                    return i
        if update[index] == rule[0]:
            for i in range(index):
                if update[i] == rule[1]:
                    return i
    return -1

def fixOrder(update, rules):
    i = 0
    while i < len(update):
        p = checkRules(i, update, rules)
        if p != -1:
            update[i], update[p] = update[p], update[i]
            i = 0
        else:
            i+= 1
    return update


sum = 0
for update in updates:
    valid = True
    for i in range(len(update)):
        if checkRules(i, update, rules) != -1:
            valid = False
            break
    if not valid:
        upd = fixOrder(update, rules)
        sum += upd[int(len(upd)/2)]
        
print(sum)