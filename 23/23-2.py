example = [3,8,9,1,2,5,4,6,7] + list(range(10,1000001))
input =[5,3,8,9,1,4,7,6,2] + list(range(10,1000001))

import time

def shuffle(cups,rounds):
    currentCup = 0
    for m in range(1,rounds+1):
        #print(m)
        removed = cups[currentCup+1:currentCup+4]
        cups = cups[:currentCup+1] + cups[currentCup+4:]
        #print(removed,cups)
        destinationCup = cups[currentCup]
        destinationCupIndex =None
        while destinationCupIndex == None:
            destinationCup = destinationCup -1
            if destinationCup == 0:
                destinationCup = 9
            try:
                destinationCupIndex = cups.index(destinationCup)
                #print(destinationCup,destinationCupIndex)
            except:
                pass
        cups = cups[:destinationCupIndex+1] + removed + cups[destinationCupIndex+1:]
        #print(cups)
        #currentCup = currentCup+1
        #don't shift current cup shift circle?
        cups = cups[1:] + cups[0:1]
    
    #print(cups)
    index = cups.index(1)
    print(cups[index+1],cups[index+2])
    print(cups[index+1]*cups[index+2])

#100 ~ 18 seconds
#1000 ~ 140 seconds
#10,000,000 ~ 20 days
start_time = time.time()
shuffle(example.copy(),100)
print("%s seconds" % (time.time() - start_time))

start_time = time.time()
shuffle(input.copy(),100)
print("%s seconds" % (time.time() - start_time))