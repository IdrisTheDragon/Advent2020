

def part1(min,max,letter,password):
    lcount = 0
    for y in password:
        if letter == y:
            lcount = lcount+1
    if int(min) <= lcount and lcount <= int(max):
        return 1
    return 0

def part2(min,max,letter,password):
    if (password[int(min)-1] != letter and password[int(max)-1] == letter) or (password[int(min)-1] == letter and password[int(max)-1] != letter):
        return 1
    return 0

f = open("input.txt", "r")
part1Count = 0
part2Count = 0
for x in f:
    m = x.split()
    min,max = m[0].split('-')
    letter = m[1][0]
    password = m[2]
    #print(min,max,letter,password)
    part1Count = part1Count + part1(min,max,letter,password)
    part2Count = part2Count + part2(min,max,letter,password)

print(part1Count)
print(part2Count)