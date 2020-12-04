
fields = ["byr" ,
"iyr" ,
"eyr",
"hgt" ,
"hcl" ,
"ecl" ,
"pid"]

def part1(l):
    count = 0
    passport = ""
    for x in l:
        if x == '\n':
            valid = True
            for y in fields:
                
                if y not in passport:
                    valid = False
            if valid:
                count = count + 1
            passport = ""
        else:
            passport = passport + x
    print(count)
    return count

import re

rgx = re.compile(r'(?:byr:)(?P<byr>\d+)|(?:iyr:)(?P<iyr>\d+)|(?:eyr:)(?P<eyr>\d+)|(?:hgt:)(?P<hgt>\d+)(?P<hgtu>cm|in)|(?:hcl:)(?P<hcl>#[0-9a-f]+)|(?:ecl:)(?P<ecl>[a-z]+)|(?:pid:)(?P<pid>[0-9]+)')

def part2(l):
    passport = ""
    count = 0
    for x in l:
        if x == '\n':
            byr,iyr,eyr,hgt,hgtu,hcl,ecl,pid = None,None,None,None,None,None,None,None
            valid = True
            for y in rgx.finditer(passport):
                if y.group("byr"):
                    byr=y.group("byr")
                elif y.group("iyr"):
                    iyr = y.group("iyr")
                elif y.group("eyr"):
                    eyr = y.group("eyr")
                elif y.group("hgt"):
                    hgt = y.group("hgt")
                    hgtu = y.group("hgtu")
                elif y.group("hcl"):
                    hcl = y.group("hcl")
                elif y.group("ecl"):
                    ecl = y.group("ecl")
                elif y.group("pid"):
                    pid = y.group("pid")
            print(byr,iyr,eyr,hgt,hgtu,hcl,ecl,pid)

            #  byr (Birth Year)
            if byr is None or not 1920 <= int(byr) <= 2002:
                valid = False
            #   iyr (Issue Year)
            if iyr is None or not 2010 <= int(iyr) <= 2020:
                valid = False
            #   eyr (Expiration Year)
            if eyr is None or not 2020 <= int(eyr) <= 2030:
                valid = False
             #   hgt (Height)
            if hgt is None or hgtu is None or not ((hgtu == "cm" and 150 <= int(hgt) <=193) or (hgtu == "in" and 59 <= int(hgt) <=76)):
                valid = False
            #   hcl (Hair Color)
            if hcl is None or len(hcl) is not 7:
                valid = False
            #   ecl (Eye Color)
            if ecl is None or ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid = False
            #   pid (Passport ID)
            if pid is None or len(pid) is not 9:
                valid = False
            print(valid)
            if valid:
                count = count + 1
            passport = ""
        else:
            passport = passport + x
    print(count)
    return count
        


#f = open("example.txt", "r")
f = open("input.txt", "r")
l = []
for x in f:
    l.append(x)
#part1(l)
part2(l)
