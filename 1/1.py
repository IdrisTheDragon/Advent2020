def part1(i):
    for x in i:
        for y in i:
            if y + x == 2020:
                print(y*x)
                return

def part2(i):
    for x in i:
        for y in i:
            for z in i:
                if y + x + z == 2020:
                    print(y*x*z)
                    return


f = open("input.txt", "r")
l = []
for x in f:
    l.append(int(x))

part1(l)
part2(l)