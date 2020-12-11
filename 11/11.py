def prettyPrint(l):
    for x in l:
        print(x)

neighbour = [(-1,-1),(-1,0),(-1,1),
                (0,-1),          (0,1),
                 (1,-1), (1,0), (1,1)]

def part1Helper(x,y,s,r,l):
    neighbors = 0
    for n in neighbour:
        nx = x
        ny = y

        nx = nx + n[0]
        ny = ny + n[1]

        if 0 <= nx <= len(l)-1 and 0 <= ny <= len(r)-1 and l[nx][ny] == '#':
            neighbors = neighbors+1
        #print(nx,ny)
    return neighbors

def part2Helper(x,y,s,r,l):
    neighbors = 0
    for n in neighbour:
        nx = x
        ny = y

        while True:
            nx = nx + n[0]
            ny = ny + n[1]

            if 0 <= nx <= len(l)-1 and 0 <= ny <= len(r)-1:
                if l[nx][ny] == '#':
                    neighbors = neighbors+1
                    break
                elif l[nx][ny] == 'L':
                    break
            else:
                break
        #print(nx,ny)
    return neighbors

def round(part,l):
    m = []
    changes = 0
    for x,r in enumerate(l):
        mr = ''
        for y ,s in enumerate(r):
            if y == '.':
                mr = mr + '.'
            else:
                if part ==2:
                    neighborLimit = 5
                    neighbors = + part2Helper(x,y,s,r,l)
                else:
                    neighbors = + part1Helper(x,y,s,r,l)
                    neighborLimit = 4
                #print(x,y,s,neighbors)
                if s == 'L' and neighbors == 0:
                    changes = changes +1
                    mr = mr + '#'
                elif s == '#' and neighbors >= neighborLimit:
                    changes = changes +1
                    mr = mr + 'L'
                else:
                    mr = mr + s
        m.append(mr)
    return m, changes == 0

def part(part,l):
    changes = False
    while not changes:
        m, changes = round(part,l)
        l = m
    #prettyPrint(l)

    count = 0
    for r in l:
        for s in r:
            if s == '#':
                count = count +1
    print(count)


#f = open("example.txt", "r")
f = open("input.txt", "r")
l = []
for x in f:
    l.append(x[:-1])

part(1,l)
part(2,l)