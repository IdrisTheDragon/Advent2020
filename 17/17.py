def prettyPrint(l,layer):
    for y in l[layer]:
        for x in y:
            print(x,end='')
        print()

def nextCube(x,y,z,l):
    activeN = 0
    inactiveN = 0

    for az in [-1,0,1]:
        for ay in [-1,0,1]:
            for ax in [-1,0,1]:
                nx = x - 1
                ny = y - 1
                nz = z - 1
                nx = nx + ax
                ny = ny + ay
                nz = nz + az

                if az == 0 and ay == 0 and ax == 0:
                    continue

                #print(nz,ny,nx)
         
                if 0 <= nz <= len(l) - 1 and 0 <= ny <= len(l[nz]) - 1 and 0 <= nx <= len(l[nz])-1 and l[nz][ny][nx] == '#':
                    activeN = activeN + 1
                else:
                    inactiveN = inactiveN + 1

    curCell = '.'
    if 0 <= z-1 <= len(l) - 1 and 0 <= y-1 <= len(l[z-1]) - 1 and 0 <= x-1 <= len(l[z-1][y-1]) - 1:
        curCell = l[z-1][y-1][x-1]


    if curCell == '#' and (activeN ==2 or activeN == 3):
        return '#'
    elif curCell == '.' and activeN == 3:
        return '#'
    else:
        return '.'


def part1(l,startSize):
    zMax = 0
    xyMax = startSize
    cycle = 1 
    
    while cycle <=6:
        cycle = cycle+1
        zMax = zMax + 2
        xyMax = xyMax + 2
        print('cycle',cycle-1)
        temp = []
        for z in range(0,zMax+1):
            temp.append([])
            for y in range(0,xyMax+1):
                tempY = []
                for x in range(0,xyMax+1):
                    tempY.append(nextCube(x,y,z,l))
                    pass
                temp[z].append(tempY)
            print('layer',(-zMax/2) + z )
            prettyPrint(temp,z)
        print()
        l = temp
        
    
    activeCount = 0
    for z in range(0,zMax+1):
        for y in range(0,xyMax+1):
            for x in range(0,xyMax+1):
                if l[z][y][x] == '#':
                    activeCount = activeCount+1
    print(activeCount)

#startSize = 3
#f = open("example.txt", "r")

startSize = 8
f = open("input.txt", "r")
l = []
l.append([])
for x in f:
    l[0].append(x[:-1])

prettyPrint(l,0)

part1(l,startSize)