import time
import array

def part(l,lim):
    l = l[0].split(',')
    spoke = {}
    lastNum = 0
    turn = 0
    for n,x in enumerate(l):
        lastNum = int(x)
        turn = n+1
        spoke[lastNum] = [turn]
    while turn != lim:
        turn = turn + 1

        #print(spoke)
        #print(turn,lastNum)

        c = spoke[lastNum]
        if len(c) == 1:
            lastNum = 0
            
        elif len(c) == 2:
            lastNum = c[1] - c[0]
        else:
            print("goofed up")
        if lastNum in spoke.keys():
            d = spoke[lastNum]
            d = [d[-1],turn]
            spoke[lastNum] = d
        else:
            spoke[lastNum] = [turn]
        
    #print(spoke)
    print(turn,lastNum)

def optimised(l,lim):
    l = l[0].split(',')
    spoke = {}
    nextNum = 0
    prevNum=0
    turn = 0
    for n,x in enumerate(l[:-1]):
        nextNum = int(x)
        turn = n+1
        spoke[nextNum] = turn
    nextNum = int(l[-1])
    while turn != lim:
        turn = turn + 1
        #print(spoke)
        #print(turn,nextNum)
        pT = spoke.get(nextNum,turn)
        spoke[nextNum] = turn
        prevNum = nextNum
        nextNum = turn - pT      
    #print(spoke)
    print(turn,prevNum)

def optimised1(l,lim):
    l = l[0].split(',')
    spoke = array.array('I', [0]) * lim
    nextNum = 0
    prevNum=0
    turn = 0
    for n,x in enumerate(l[:-1]):
        nextNum = int(x)
        turn = n+1
        spoke[nextNum] = turn
    nextNum = int(l[-1])
    for turn in range(turn+1, lim+1):
        #print(spoke)
        #print(turn,nextNum)
        pT = spoke[nextNum]
        spoke[nextNum] = turn
        prevNum = nextNum
        nextNum = 0 if pT == 0 else turn - pT      
    #print(spoke)
    print(turn,prevNum)

#f = open("example.txt", "r")
f = open("input.txt", "r")
#f = open("example2.txt", "r")

l = []
for x in f:
    l.append(x)

part(l,2020)

start_time = time.time()
part(l,30000000)
print("Original: %s seconds" % (time.time() - start_time))

start_time = time.time()
optimised(l,30000000)
print("Optimised: %s seconds" % (time.time() - start_time))

start_time = time.time()
optimised1(l,30000000)
print("Optimised1: %s seconds" % (time.time() - start_time))