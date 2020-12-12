import math

def part1(l):
    shipDir = 0
    shipPos = [0,0]
    for x in l:
        if x[0] == 'N':
            shipPos[1] = shipPos[1] + x[1]
        elif x[0] == 'S':
            shipPos[1] = shipPos[1] - x[1]
        elif x[0] == 'E':
            shipPos[0] = shipPos[0] + x[1]
        elif x[0] == 'W':
            shipPos[0] = shipPos[0] - x[1]
        elif x[0] == 'R':
            shipDir = shipDir - x[1]
        elif x[0] == 'L':
            shipDir = shipDir + x[1]
        elif x[0] == 'F':
            O = math.sin(math.radians(shipDir)) * x[1]
            A = math.cos(math.radians(shipDir)) * x[1]
            shipPos[1] = shipPos[1] + int(O)
            shipPos[0] = shipPos[0] + int(A)
        print(x)
        print(shipPos)

    print(abs(shipPos[0])+abs(shipPos[1]))

def part2(l):
    shipPos = [0,0]
    wayPointPos = [10,1]
    for x in l:
        if x[0] == 'N':
            wayPointPos[1] = wayPointPos[1] + x[1]
        elif x[0] == 'S':
            wayPointPos[1] = wayPointPos[1] - x[1]
        elif x[0] == 'E':
            wayPointPos[0] = wayPointPos[0] + x[1]
        elif x[0] == 'W':
            wayPointPos[0] = wayPointPos[0] - x[1]
        elif x[0] == 'L':
            newX = wayPointPos[0] * int(math.cos(math.radians(x[1]))) - wayPointPos[1] * int(math.sin(math.radians(x[1])))
            newY = wayPointPos[1] * int(math.cos(math.radians(x[1]))) + wayPointPos[0] * int(math.sin(math.radians(x[1])))
            wayPointPos[0] = int(newX)
            wayPointPos[1] = int(newY)
        elif x[0] == 'R':
            newX = wayPointPos[0] * int(math.cos(math.radians(-x[1]))) - wayPointPos[1] * int(math.sin(math.radians(-x[1])))
            newY = wayPointPos[1] * int(math.cos(math.radians(-x[1]))) + wayPointPos[0] * int(math.sin(math.radians(-x[1])))
            wayPointPos[0] = newX
            wayPointPos[1] = newY
        elif x[0] == 'F':
            shipPos[0] = shipPos[0] + (wayPointPos[0] * x[1])
            shipPos[1] = shipPos[1] + (wayPointPos[1] * x[1])
        
        print(x)
        print(shipPos,wayPointPos)

    print(abs(shipPos[0])+abs(shipPos[1]))


#f = open("example.txt", "r")
f = open("input.txt", "r")
l = []
for x in f:
    l.append((x[0],int(x[1:-1])))

#28591
#part1(l)
part2(l)