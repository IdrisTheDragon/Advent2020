

def prettyPrint(l):
    for x in l:
        print(x)

def part1Helper(x,y,s,r,l):
    neighbor = [(-1,-1),(-1,0),(-1,1),
                (0,-1),          (0,1),
                 (1,-1), (1,0), (1,1)]
    neighbors = 0
    for n in neighbor:
        nx = x
        ny = y

        nx = nx + n[0]
        ny = ny + n[1]

        if 0 <= nx <= len(l)-1 and 0 <= ny <= len(r)-1 and l[nx][ny] == '#':
            neighbors = neighbors+1

        #print(nx,ny)

    return neighbors

def part1Round(l):
    m = []
    changes = 0
    for x,r in enumerate(l):
        mr = ''
        for y ,s in enumerate(r):
            if y == '.':
                mr = mr + '.'
            else:
                neighbors = part1Helper(x,y,s,r,l)
                #print(x,y,s,neighbors)
                if s == 'L' and neighbors == 0:
                    changes = changes +1
                    mr = mr + '#'
                elif s == '#' and neighbors >=4:
                    changes = changes +1
                    mr = mr + 'L'
                else:
                    mr = mr + s
        m.append(mr)
    return m, changes == 0

def part1(l):
    changes = False
    while not changes:
        m, changes = part1Round(l)
        #print(changes)
        l = m
    #prettyPrint(l)

    count = 0
    for r in l:
        for s in r:
            if s == '#':
                count = count +1
    print(count)

def part2Helper(x,y,s,r,l):
    neighbor = [(-1,-1),(-1,0),(-1,1),
                (0,-1),          (0,1),
                 (1,-1), (1,0), (1,1)]
    neighbors = 0
    for n in neighbor:
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



def part2Round(l):
    m = []
    changes = 0
    for x,r in enumerate(l):
        mr = ''
        for y ,s in enumerate(r):
            if y == '.':
                mr = mr + '.'
            else:
                neighbors = + part2Helper(x,y,s,r,l)
                #print(x,y,s,neighbors)
                if s == 'L' and neighbors == 0:
                    changes = changes +1
                    mr = mr + '#'
                elif s == '#' and neighbors >=5:
                    changes = changes +1
                    mr = mr + 'L'
                else:
                    mr = mr + s
        m.append(mr)
    return m, changes == 0

def part2(l):
    changes = False
    while not changes:
        m, changes = part2Round(l)
        l = m
    #prettyPrint(l)

    count = 0
    for r in l:
        for s in r:
            if s == '#':
                count = count +1
    print(count)


#f = open("example.txt", "r")
#f = open("example2.txt", "r")
f = open("input.txt", "r")
l = []
for x in f:
    l.append(x[:-1])

part1(l)
part2(l)