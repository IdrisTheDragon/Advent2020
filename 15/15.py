
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
        

    
    

#f = open("example.txt", "r")
f = open("input.txt", "r")
#f = open("example2.txt", "r")

l = []
for x in f:
    l.append(x)

part(l,2020)
part(l,30000000)