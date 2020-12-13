
def part1(curTime,busTimes):
    remainders = []
    smallestRemainder = 500000
    smallestRemainderIndex = 0
    for n,x in enumerate(busTimes):
        if x == 'x':
            remainders.append(500000)
        else:
            x = int(x)
            r = curTime%x
            r1 = -r+x
            remainders.append(r1)
        if remainders[n] < smallestRemainder:
            smallestRemainder = remainders[n]
            smallestRemainderIndex = n
    print(smallestRemainderIndex,smallestRemainder,busTimes[smallestRemainderIndex],smallestRemainder*int(busTimes[smallestRemainderIndex]))

def part2(busTimes):
    t = 0
    product = 1 # product of the previous ids.

    for n, x in enumerate(busTimes):
        if x == 'x':
            continue
        x = int(x)
        while((t + n) % x != 0):
            t += product #increase t by product, ensures 
        product *= x
    print(t)



#f = open("example.txt", "r")
f = open("input.txt", "r")

l = []
for x in f:
    l.append(x)

curTime = int(l[0][:-1])
busTimes = l[1][:-1].split(',')

#print(curTime,busTimes)

#part1(curTime,busTimes)
part2(busTimes)