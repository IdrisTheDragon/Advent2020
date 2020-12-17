def prettyPrint(l,layer):
    for y in l[layer]:
        for x in y:
            print(x,end='')
        print()

neighbour = [ (-1,-1,-1),(-1,0,-1),(-1,1,-1),
                (0,-1,-1), (0,0,-1) ,(0,1,-1),
                (1,-1,-1), (1,0,-1), (1,1,-1),
    
                (-1,-1,0),(-1,0,0),(-1,1,0),
                (0,-1,0),          (0,1,0),
                (1,-1,0), (1,0,0), (1,1,0),
                 
                (-1,-1,1),(-1,0,1),(-1,1,1),
                (0,-1,1), (0,0,1), (0,1,1),
                (1,-1,1), (1,0,1), (1,1,1)]

def nextCube(x,y,z,l):
    activeN = 0
    inactiveN = 0

    debug = z == 0 and y ==4 and x ==4

    for n in neighbour:
        nx = x - 1
        ny = y - 1
        nz = z
        nx = nx + n[0]
        ny = ny + n[1]
        nz = nz + n[2]

        
            

        if nz in l.keys():
            zLayer = l[nz]
            if 0 <= ny <= len(zLayer) - 1 and 0 <= nx <= len(zLayer[ny])-1 and zLayer[ny][nx] == '#':
                activeN = activeN + 1
            else:
                inactiveN = inactiveN + 1
        else:
            inactiveN = inactiveN + 1

    curCell = '.'
    if z in l.keys() and 0 <= y-1 <= len(l[z]) - 1 and 0 <= x-1 <= len(l[z][y-1]) - 1:
        curCell = l[z][y-1][x-1]


    if curCell == '#' and (activeN ==2 or activeN == 3):
        return '#'
    elif curCell == '.' and activeN == 3:
        return '#'
    else:
        return '.'


def part1(l,startSize):
    zMin = 0
    zMax = 0
    xMax = startSize
    yMax = startSize
    cycle = 1 
    
    while cycle <= 6:
        cycle = cycle+1
        zMin = zMin - 1
        zMax = zMax + 1
        xMax = xMax + 2
        yMax = yMax + 2
        #print('cycle',cycle-1)
        temp = {}
        for z in range(zMin,zMax+1):
            temp[z] = []
            for y in range(0,yMax+1):
                tempY = []
                for x in range(0,xMax+1):
                    tempY.append(nextCube(x,y,z,l))
                    pass
                temp[z].append(tempY)
            #print('layer',z)
            #prettyPrint(temp,z)
        #print()
        l = temp
        
    
    activeCount = 0
    for z in range(zMin,zMax+1):
        for y in range(0,yMax+1):
            for x in range(0,xMax+1):
                if l[z][y][x] == '#':
                    activeCount = activeCount+1
    print(activeCount)

#startSize = 3
#f = open("example.txt", "r")

startSize = 8
f = open("input.txt", "r")
l = {}
l[0] = []
for x in f:
    l[0].append(x[:-1])

#prettyPrint(l,0)

part1(l,startSize)