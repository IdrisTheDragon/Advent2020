def part1(p1,p2):
    round = 0
    while len(p1) > 0 and len(p2)>0 and round <400:
        round = round + 1
        #print(p1)
        #print(p2)
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 >c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    #print(round)
    #print(p1)
    #print(p2)
    if len(p1) > 0:
        return p1
    else:
        return p2

def part2(p1,p2, gameIndex):
    prevRounds = []
    roundIndex = 1
    while len(p1) > 0 and len(p2)>0:
        #print('g', gameIndex,roundIndex)
        #print(p1)
        #print(p2)
        sp1 = ' '.join([str(num) for num in p1])
        sp2 = ' '.join([str(num) for num in p2])
        if (sp1,sp2) in prevRounds:
                return p1, True
        c1 = p1.pop(0)
        c2 = p2.pop(0)

        #print(c1,c2,len(p1),len(p2))

        if c1 <= len(p1) and c2 <= len(p2):
            #print('recursive')
            d,p = part2(p1.copy()[:c1],p2.copy()[:c2], gameIndex+1)
        else:
            p = c1 >c2
        
        if p:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
        prevRounds.append((sp1,sp2))
        roundIndex =roundIndex +1

    if len(p1) > 0:
        return p1, True
    else:
        return p2, False



#f = open("example.txt", "r")
#f = open("example1.txt", "r")
f = open("input.txt", "r")
p1 = []
p2 = []
p2t = False
for x in f:
    if x[0] == 'P':
        pass
    elif x =='\n':
        p2t = True
    elif p2t:
        p2.append(int(x))
    else:
        p1.append(int(x))
print(p1)
print(p2)

#w = part1(p1,p2)
w,p = part2(p1,p2,1)

sum = 0
i = len(w)
for x in w:
    sum = sum + x*i
    i=i-1

print(sum)
