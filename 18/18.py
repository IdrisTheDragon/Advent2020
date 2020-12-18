



def calc(x):
    result = 0
    operation = ''
    offset=0
    for y in range(0,len(x)):
        y = y+offset
        if y == len(x):
            break

        cur = x[y]
        value = None
        if cur == '(':
            value,off = calc(x[y+1:])
            offset = offset + off
        elif cur == ')':
            return result,y+1
        elif cur in ['+','*']:
            operation = cur
        elif cur == ' ':
            pass
        else:
            #print(cur)
            value = int(cur)
        
        if value != None:
            if operation == '':
                result = value
            elif operation == '+':
                result = result + value
            elif operation == '*':
                result = result * value
        #print(result,value,x[y:])
    return result


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def calc2(x):
    stopINf = 0
    while not RepresentsInt(x) and stopINf < 2000:
        stopINf = stopINf + 1
        #print(x) 
        try:
            index = x.index('(')
            stack = ['(']
            i=index
            while len(stack) != 0:
                i = i+1
                if x[i] == ')':
                    stack.pop()
                elif x[i] == '(':
                    stack.append('(')
            p = x[index+1:i]
            r = calc2(p)

            x = x[:index] + str(r) + x[i+1:]
            # print(x)
            continue
        except:
            pass
        try:
            index = x.index('+')
            i = index-2
            v1 = ''
            while i != -1 and  x[i] != ' ':
                v1 = x[i] + v1 
                i=i-1
            j = index+2
            v2 = ''
            while j != len(x) and x[j] != ' ':
                v2 = v2 + x[j]
                j=j+1
            v1 = int(v1)
            v2 = int(v2)
            r = v1 + v2
            x = x[:i+1] + str(r) + x[j:]
            continue
        except:
            pass
        try:
            index = x.index('*')
            i = index-2
            v1 = ''
            while i != -1 and  x[i] != ' ':
                v1 = x[i] + v1
                i=i-1
            j = index+2
            v2 = ''
            while j != len(x) and x[j] != ' ':
                v2 = v2 + x[j]
                j=j+1
            v1 = int(v1)
            v2 = int(v2)
            r = v1 * v2
            #print(v1,v2)
            x = x[:i+1] + str(r) + x[j:]
            continue
        except:
            pass
        

    return int(x)

def part2(l):
    sum =0
    for x in l:
        result = calc2(x)
        #print(x,result)
        sum = sum + result
    print(sum)   


def part1(l):
    sum =0
    for x in l:
        result = calc(x)
        #print(x,result)
        sum = sum + result
    print(sum)

#f = open("example.txt", "r")

f = open("input.txt", "r")
l = []
for x in f:
    l.append(x[:-1])


#print(l)

# r = calc2('1 + 1')
# print(r,2)

# r = calc2('(1 + 1) + 1')
# print(r,3)
# r = calc2('(1 * 1) + 1')
# print(r,2)
# r = calc2('2 * 1 + 3')
# print(r,8)

part1(l)
part2(l)