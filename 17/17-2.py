def prettyPrint(l,layer):
    for y in l[layer]:
        for x in y:
            print(x,end='')
        print()

def nextCube(x,y,z,w,l):
    activeN = 0
    inactiveN = 0
    for aw in [-1,0,1]:
        for az in [-1,0,1]:
            for ay in [-1,0,1]:
                for ax in [-1,0,1]:
                    nx = x - 1
                    ny = y - 1
                    nz = z - 1
                    nw = w-1
                    nx = nx + ax
                    ny = ny + ay
                    nz = nz + az
                    nw = nw + aw

                    if aw == 0 and az == 0 and ay == 0 and ax == 0:
                        continue

            
                    if 0 <= nw <= len(l) - 1 and 0 <= nz <= len(l[nw]) - 1 and 0 <= ny <= len(l[nw][nz]) - 1 and 0 <= nx <= len(l[nw][nz][ny])-1 and l[nw][nz][ny][nx] == '#':
                        activeN = activeN + 1
                    else:
                        inactiveN = inactiveN + 1

    curCell = '.'
    if 0 <= w-1 <= len(l) - 1 and 0 <= z-1 <= len(l[w-1]) - 1 and 0 <= y-1 <= len(l[w-1][z-1]) - 1 and 0 <= x-1 <= len(l[w-1][z-1][y-1]) - 1:
        curCell = l[w-1][z-1][y-1][x-1]


    if curCell == '#' and (activeN ==2 or activeN == 3):
        return '#'
    elif curCell == '.' and activeN == 3:
        return '#'
    else:
        return '.'


def part1(l,startSize):
    zwMax = 0
    xyMax = startSize
    cycle = 1 
    
    while cycle <=6:
        cycle = cycle+1
        zwMax = zwMax + 2
        xyMax = xyMax + 2
        #print('cycle',cycle-1)
        temp = []
        for w in range(0,zwMax+1):
            tempW = [] # w
            for z in range(0,zwMax+1):
                tempZ = [] # z
                for y in range(0,xyMax+1):
                    tempY = [] # y
                    for x in range(0,xyMax+1):
                        tempY.append(nextCube(x,y,z,w,l)) # y[x]
                        pass
                    tempZ.append(tempY)  # z[y]
                tempW.append(tempZ)
            temp.append(tempW)
        l = temp
        
    
    activeCount = 0
    print(len(l), len(l[0]), len(l[0][0]), len(l[0][0][0]), l[0][0][0][0])
    for w in range(0,zwMax+1):
        for z in range(0,zwMax+1):
            for y in range(0,xyMax+1):
                for x in range(0,xyMax+1):
                    if l[w][z][y][x] == '#':
                        activeCount = activeCount+1
    print(activeCount)

#startSize = 3
#f = open("example.txt", "r")

startSize = 8
f = open("input.txt", "r")
l = []
l.append([])
l[0].append([])
for x in f:
    l[0][0].append(x[:-1])


print(len(l), len(l[0]), len(l[0][0]), len(l[0][0][0]), l[0][0][0][0])
part1(l,startSize)