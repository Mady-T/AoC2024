file = open('inputs/day7inp1')
rawinp = file.read().strip()
file.close()

equations = rawinp.split("\n")
for i in range(len(equations)):
    equations[i] = equations[i].split(':')
    equations[i][1] = equations[i][1].split()
    equations[i][0] = int(equations[i][0])
    for j in range(len(equations[i][1])):
        equations[i][1][j] = int(equations[i][1][j])

# format of equations:= [target, [operand, operand, operand ... operand]]

def checkValid(operands, target, index = 0, value = 0):
    if index < len(operands):
        if index == 0:
            value += operands[index]
            index += 1
            return checkValid(operands, target, index, value)
        else:
            add_value = value + operands[index]
            mul_value = value * operands[index]
            cat_value = int(str(value) + str(operands[index]))
            index += 1
            if checkValid(operands, target, index, add_value):
                return True
            elif checkValid(operands, target, index, mul_value):
                return True
            else:
                return checkValid(operands, target, index, cat_value)

    else:
        if value == target:
            return True
        else:
            return False
        
num_valid = 0
sum = 0
for i in range(len(equations)):
    if checkValid(equations[i][1],equations[i][0]):
        num_valid+=1
        sum+=equations[i][0]

print(sum)