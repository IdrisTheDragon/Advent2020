def executeInstruction(l,n,acc):
    if len(l) == n:
        #print("end of instructions")
        return acc, True
    if l[n].executionCount > 0:
        # print("infintie loop")
        return acc, False

    # print(l[n],'|',n,acc)
    
    l[n].executionCount = l[n].executionCount + 1 
    if l[n].instruction == 'acc':
        acc = acc + l[n].value
    if l[n].instruction == 'jmp':
        n = n+l[n].value
    else:
        n=n+1
    return executeInstruction(l,n,acc)

class Instruction:
    def __init__(self, instruction, value):
        self.instruction = instruction
        self.value = value
        self.executionCount=0
    
    def __str__(self):
        return self.instruction + ',' + str(self.value) + ',' + str(self.executionCount)



#f = open("example2.txt", "r")
#f = open("example.txt", "r")
f = open("input.txt", "r")
l = []
max = 0
for x in f:
    i,v = x.split(' ')
    l.append(Instruction(instruction=i,value=int(v)))

print('part1')
print(executeInstruction(l,0,0)[0])

print('part2')
for num,x in enumerate(l):
    for y in l:
        y.executionCount = 0

    change = False
    #change instruction
    if x.instruction == 'jmp':
        x.instruction = 'nop'
        #print(num,'nop')
        change = True
    elif x.instruction == 'nop':
        change = True
        #print(num,'jmp')
        x.instruction = 'jmp'
    # run the thing, is it infinite?
    if change:
        acc, notinf = executeInstruction(l,0,0)
        if notinf:
            print(acc)
            break

        # change it back cause it didn't fix the thing
        if x.instruction == 'jmp':
            x.instruction = 'nop'
        elif x.instruction == 'nop':
            x.instruction = 'jmp'
