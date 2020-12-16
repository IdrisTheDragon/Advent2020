
def not_blank_or_or(v):
    return v not in['','or']


def validate(rules,tickets):
    invalidField = []
    validTickets = [tickets[0]]
    for ticket in tickets[1:]:
        v = True
        for ticketValue in ticket:
            valid = False
            for rule in rules.values():
                for range in rule:
                    r = range.split('-')
                    if int(r[0]) <= int(ticketValue) <= int(r[1]):
                        valid = True
                        break
                if valid: break
            if not valid:
                invalidField.append(int(ticketValue))
                v = False
        if v:
            validTickets.append(ticket)
            
    #print(invalidField)
    print(sum(invalidField))
    return validTickets

def meetRule(key,ticketValue, rules):
    rule = rules[key]
    valid = False
    for range in rule:
        r = range.split('-')
        if int(r[0]) <= int(ticketValue) <= int(r[1]):
            valid = True
            break
    return valid

def resolveFields(rules,tickets):
    options = []
    for i in range(0,len(rules)):
        options.append(rules.keys())
    #print(options)
    for ticket in tickets:
        for i,ticketValue in enumerate(ticket):
            ticketValue = int(ticketValue)
            options[i] = list(filter(lambda x:( meetRule(x,ticketValue, rules) ) ,options[i]))

    #options.sort(key=lambda x:len(x))
    #print(options)
    finished = []
    i = 0
    while len(finished) != len(options):
        o = options[i]
        #print(o)
        if len(o) == 1 and o[0] not in finished:
            finished.append(o[0])
            for j in range(0,len(options)):
                if len(options[j]) != 1:
                    options[j] = list(filter(lambda x: (x != o[0]), options[j]))
        i = i + 1
        if i == len(options): i=0

    for k in range(0,len(options)):
        options[k] = options[k][0]
        
    print(options)

    sum = 1

    for i,r in enumerate(options):
        if 'departure' in r:
            sum = sum * int(tickets[0][i])
    print(sum)
            





#f = open("example.txt", "r")
f = open("input.txt", "r")
#f = open("example1.txt", "r")

rules = {}
tickets = []
endRules = False
for x in f:
    if x in ['\n','your ticket:\n','nearby tickets:\n']:
        endRules = True
    elif endRules:
        
        tickets.append(x[:-1].split(','))
    else:
        c = x.split(':')
        d = c[1][:-1].split(' ') 
        d = list(filter(not_blank_or_or,d))
        rules[c[0]] = d

validTickets = validate(rules,tickets)
#print(validTickets)

resolveFields(rules,validTickets)