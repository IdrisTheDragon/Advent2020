import re
import time


def finishedStr(strg, search=re.compile(r'[^ab\(\)\| ]').search):
    return not bool(search(strg))


def compileR(rules):
    finished = False
    while not finished:
        finished = True
        for x, rule in rules.items():
            if x ==14:
                print(14)
            if finishedStr(rule):
                #aaabaa etc
                for y,r in rules.items():
                    if r.__contains__(str(x)):
                        r = re.sub(r'\b' + str(x) + r'\b', '('+rule+')',r)
                    rules[str(y)] = r
            else:
                # not aabaa etc
                finished = False
                pass
        # time.sleep(1)
        # print(rules)   
        # print()
    return rules


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
        num = z[0]
        rs = z[1].strip()
        
        if rs.__contains__('"'):
            rs = rs.strip().strip('"')
        rules[num] = rs
    else:
        l.append(x[:-1])

#print(rules) 

# print('a', finishedStr('a'))
# print('14', finishedStr('14'))
# print(' 14 ', finishedStr(' 14 '))
# print('ab | 12', finishedStr('ab | 12'))
# print('ab | ab', finishedStr('ab | ab'))
# print('ab | (ab)', finishedStr('ab | (ab)'))

# r = '14'
# print(r)
# r = re.sub(r'\b' + str(14) + r'\b', '(a)',r)
# print(r)

rules['8'] = "|".join("42 " * i for i in range(1, 10))
rules['11'] = "|".join("42 " * i + "31 " * i for i in range(1, 10))
compiledRules = compileR(rules)

rule = '^' + compiledRules['0'].replace(" ", "") + '$'
#print(rule)
reg = re.compile(rule)
sum = 0
for x in l:
    if reg.match(x):
        sum = sum+1
print(sum)