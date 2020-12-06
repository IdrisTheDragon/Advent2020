

def part1(l):
    sum = 0
    combined = set()
    for x in l:
        if x == '\n':
            #print(combined)
            sum = sum + len(combined)
            combined = set()
        else:
            for y in x[:-1]:
                combined.add(y)
    print(sum)

def part2(l):
    sum = 0
    combined = set()
    newGroup = True
    for x in l:
        if x == '\n':
            #print(combined)
            sum = sum + len(combined)
            combined = set()
            newGroup = True
        elif newGroup:
            for y in x[:-1]:
                combined.add(y)
            newGroup = False
        else:
            removal = set()
            for y in combined:
                if y not in x:
                    removal.add(y)
            for y in removal:
                combined.remove(y)
    print(sum)

#f = open("example.txt", "r")
f = open("input.txt", "r")
l = []
max = 0
for x in f:
    l.append(x)

part1(l)
part2(l)