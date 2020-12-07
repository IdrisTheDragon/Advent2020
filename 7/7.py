

def part1(l, bagColour):
    count = set()
    for key, x in l.items():
        for y in x:
            if bagColour in y:
                count.add(key)
                count.update(part1(l, key))
    return count

def part2(l, bagColour):
    count = 0
    contents = l[bagColour]
    for y in contents:
        if 'n' != y[0]:
            num = int(y[0])
            if num == 1:
                colour = y[2:-4]
            else:
                colour = y[2:-5]
            #print(num,colour)
            count = count + num
            count = count + num * part2(l,colour)
    return count


#f = open("example2.txt", "r")
#f = open("example.txt", "r")
f = open("input.txt", "r")
l = dict()
max = 0
for x in f:
    key,y = x.split(' bags contain ')
    bags = y[:-2].split(', ')
    #print(key,bags)
    l[key] = bags
    
#print(l)

count = part1(l,'shiny gold')
print(len(count))

count = part2(l,'shiny gold')
print(count)