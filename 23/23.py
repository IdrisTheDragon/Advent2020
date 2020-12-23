example = [3,8,9,1,2,5,4,6,7]
input =[5,3,8,9,1,4,7,6,2]


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
    cups = cups[index+1:] + cups[:index]
    result = ''
    for c in cups:
        result = result + str(c)
    print(result)



shuffle(example.copy(),10)
shuffle(example.copy(),100)
shuffle(input.copy(),100)