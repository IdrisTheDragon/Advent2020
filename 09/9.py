def validate(l,x):
    for y in l:
        for z in l:
            if y+z == x:
                return True
    return False

def part1(l,peramble):
    min,max = 0,preamble

    for x in l[preamble:]:
        #print(l[min:max])
        if not validate(l[min:max],x):
            print('not valid:',x)
            return x
        min=min+1
        max=max+1

def part2(l,weakness):
    min,max,prevMax = 0,2,2
    values = l[min:max]
    while(weakness != sum(values)):
        max = max+1
        min = min+1
        if max >= len(l):
            min = 0
            prevMax=prevMax+1
            max = prevMax
        values = l[min:max]
    values.sort()
    print(values)
    print(values[0]+values[-1])

#f = open("example2.txt", "r")

#preamble = 5
#f = open("example.txt", "r")

preamble = 25
f = open("input.txt", "r")
l = []
max = 0
for x in f:
    l.append(int(x))

weakness = part1(l,preamble)

part2(l,weakness)
