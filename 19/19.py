def parseR(rules, index):
    r = rules[index]
    if isinstance(r, str):
        return [r]
    else:
        options = []
        for x in r:
            xs = x.split(' ')
            variants = []
            for z in xs:
                zs = parseR(rules,int(z))
                if len(variants) == 0:
                    variants = zs
                else:
                    vs = []
                    for a in zs:
                        for b in variants:
                            vs.append(b+a)
                    variants = vs
            options = options + variants
        return options
    




#f = open("example.txt", "r")
#f = open("example1.txt", "r")
f = open("input.txt", "r")
l = []
rules = {}
rule = True
for x in f:
    if x == '\n':
        rule = False
    elif rule:
        z = x[:-1].split(':')
        num = int(z[0])
        rs = z[1].split('|')
        
        if rs[0].__contains__('"'):
            rs = rs[0].strip().strip('"')
        else:
            rss = []
            for r in rs:
               rss.append(r.strip())
            rs =rss
        rules[num] = rs
    else:
        l.append(x[:-1])

valid = parseR(rules,0)


count = 0

for x in l:
    if x in valid:
        count = count + 1
print(count)