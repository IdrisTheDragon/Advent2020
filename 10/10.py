def part1(l):
    diff1 = 0
    diff2 = 0
    diff3 = 0
    prev = 0
    for x in l:
        diff = x - prev
        if diff == 1:
            diff1 = diff1 + 1
        elif diff == 2:
            diff2 = diff2 + 1
        elif diff == 3:
            diff3 = diff3 + 1
        prev = x
    diff3 = diff3 +1
    print(diff1,diff3)
    print(diff1*diff3)

def part2(l):
    l.append(l[-1]+3)
    l = [0] + l
    l = sorted(l, reverse=True)
    r = {} 
    for n,x in enumerate(l):
        if len(r) == 0:
            r[x] = 1
        else:
            i =1
            w = 0
            while (n-i >= 0) and (l[n-i] - x <= 3):
                w += r[l[n-i]]
                i += 1
            r[x] = w
    print(r[min(r)])

#f = open("example.txt", "r")
#f = open("example2.txt", "r")
f = open("input.txt", "r")
l = []
max = 0
for x in f:
    l.append(int(x))

l.sort()

part1(l)
part2(l)