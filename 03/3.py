def part1(l,right,down):
    l = l[down::down]
    row = right
    treeCountPart1 = 0
    for x in l:
        #print(row,x[row])
        if x[row] == '#':
            treeCountPart1 = treeCountPart1 + 1
            #print(x[:row]+'X'+x[row+1:-1])
        else:
            #print(x[:row]+'O'+x[row+1:-1])
            pass
        row = row + right
        row = row % (len(x)-1)
    print(treeCountPart1)
    return treeCountPart1

def part2(l):
    a = part1(l,1,1)
    b = part1(l,3,1)
    c = part1(l,5,1)
    d = part1(l,7,1)
    e = part1(l,1,2)
    print(a*b*c*d*e)

f = open("input.txt", "r")
#f = open("example.txt", "r")
l = []
for x in f:
    l.append(x)

part1(l,3,1)
part2(l)
