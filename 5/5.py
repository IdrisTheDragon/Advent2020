

def part1(r):
    rowMin = 0
    rowMax = 127
    colMin = 0
    colMax = 7
    row,col = 0,0
    for i in r:
        if i == 'B':
            rowMin = rowMin + round((rowMax-rowMin)/2)
        elif i == 'F':
            rowMax = rowMax - round((rowMax-rowMin)/2)
        elif i == 'R':
            colMin = colMin + round((colMax-colMin)/2)
        elif i == 'L':
            colMax = colMax - round((colMax-colMin)/2)
    if(r[6] == 'B'):
        row = rowMax
    else:
        row = rowMin
    if(r[9]) == 'R':
        col = colMax
    else:
        col = colMin
    ID = (row*8)+col  
    # print(row,col,ID)
    return row,col,ID

def lsort(e):
  return e['ID']



#f = open("example.txt", "r")
f = open("input.txt", "r")
l = []
max = 0
for x in f:
    row,col,ID = part1(x)
    if max < ID:
        max = ID
    l.append({"row":row,"col":col,"ID":ID})
print(max)

l.sort(key=lsort)

for x in range(1, len(l)-1):
    if l[x]["ID"] != l[x+1]["ID"]-1:
        print(l[x],l[x+1])
        print(l[x]["ID"]+1)
        break

    
