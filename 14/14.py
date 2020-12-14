def part1(l):
    mask = ''
    mem = {}
    for x in l:
        if 'mask' in  x:
            a = x.split()
            mask = a[2]
            print(mask)
        elif 'mem' in x:
            a = x.split()
            v= a[2]
            a = a[0].split('[')
            loc = a[1][:-1]
            v = '{:036b}'.format(int(v))
            print(v)
            for n,y in enumerate(mask):
                if y == 'X':
                    pass
                else:
                    v = v[:n] + y + v[n+1:]
            mem[loc] = int(v,2)
    sum = 0
    for x in mem.values():
        sum = sum+x
    print(sum)

def breakdown(loc,v,mem,i):
    if i == len(loc):
        loc = int(loc,2)
        mem[loc] = v
    elif loc[i] == 'X':
        loc1 = loc[:i] + '1' + loc[i+1:]
        loc0 = loc[:i] + '0' + loc[i+1:]
        breakdown(loc1,v,mem,i+1)
        breakdown(loc0,v,mem,i+1)
    else:
        breakdown(loc,v,mem,i+1)


def part2(l):
    mask = ''
    mem = {}
    for x in l:
        if 'mask' in  x:
            a = x.split()
            mask = a[2]
            print(mask)
        elif 'mem' in x:
            a = x.split()
            v= int(a[2])
            a = a[0].split('[')
            loc = a[1][:-1]
            loc = '{:036b}'.format(int(loc))
            for n,y in enumerate(mask):
                if y == '0':
                    pass
                else:
                    loc = loc[:n] + y + loc[n+1:]
            breakdown(loc,v,mem,0)

    sum = 0
    for x in mem.values():
        sum = sum+x
    print(sum)      


#f = open("example.txt", "r")
f = open("input.txt", "r")
#f = open("example2.txt", "r")

l = []
for x in f:
    l.append(x)

#part1(l)
part2(l)