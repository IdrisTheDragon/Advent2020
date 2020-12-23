example = [3,8,9,1,2,5,4,6,7] + list(range(10,1000001))
input =[5,3,8,9,1,4,7,6,2] + list(range(10,1000001))

import time

def shuffle(cups,currentCup,rounds):
    for round in range(1,rounds+1):
        #print(round)
        r1 = cups[currentCup] #8
        r2 = cups[r1] #9
        r3 = cups[r2] #1
        #print(currentCup, r1,r2,r3)
        cups[currentCup] = cups[r3] 
        destinationCup = currentCup
        while destinationCup in [r1,r2,r3,currentCup]:
            destinationCup = destinationCup - 1
            if destinationCup == 0:
                destinationCup = len(cups)
        
        # add removed cups them in clockwise of destination cup
        nextCup = cups[destinationCup]
        cups[destinationCup] = r1
        cups[r3] = nextCup

        # next cup
        currentCup = cups[currentCup]

    #part1 print
    #next = cups[1]
    #result = ''
    #while next != 1:
        #result = result + str(next)
        #next = cups[next]
    #print(result)

    #part2 print
    r1 = cups[1]
    r2 = cups[r1]
    print(r1,r2,r1*r2)




#assemble dict linked list..
cups = {}
#cupsList = example
cupsList = input
for x in range(0,len(cupsList)-1):
    cups[cupsList[x]] = cupsList[x+1]

cups[cupsList[len(cupsList)-1]] = cupsList[0]
firstCup = cupsList[0]
#print(cupsList)
#print(cups)

start_time = time.time()
shuffle(cups.copy(),firstCup,10000000)
print("%s seconds" % (time.time() - start_time))