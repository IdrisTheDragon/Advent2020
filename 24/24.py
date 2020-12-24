def tileCount(tiles):
    sum = 0
    for x in tiles.values():
        if x:
            sum = sum+1
    return sum


tiles= {}


#f = open("example.txt", "r")
#f = open("example1.txt", "r")
f = open("input.txt", "r")
l = []
for x in f:
    l.append(x[:-1])

#l = ['esenee']
#l = ['nwwswee']
#l = ['esew']

#False = white
#True = black
tiles[(0,0)] = False
#print(l)
for i in l:
    prevM = ''
    coord = [0,0]
    for j in i:
        if j == 'n':
            #print('north')
            coord[1] = coord[1] - 1
        elif j == 's':
            #print('south')
            coord[1] = coord[1] + 1
        elif j == 'e':
            if prevM in ['s','n']:
                if coord[1]&1 == 0:
                    #even
                    #print('east3')
                    pass
                else:
                    #print('east2')
                    #odd
                    coord[0] = coord[0] + 1  
            else:
                #print('east')
                coord[0] = coord[0] + 1
        elif j == 'w':
            if prevM in ['s','n']:
                if coord[1]&1 == 0:
                    #print('west2')
                    #even
                    coord[0] = coord[0] - 1
                else:
                    #odd
                    #print('west3')
                    pass 
            else:
                #print('west')
                coord[0] = coord[0] - 1
        prevM = j
    coord = (coord[0],coord[1])
    #print(coord)
    if coord in tiles.keys():
        tiles[coord] = not tiles[coord]
    else:
        tiles[coord] = True
#print(tiles)

# part1
print(tileCount(tiles))
                 #  0     e      w    nw     sw    ne      se
evenNeighbours = [(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1), (1,-1)]
oddNeighbours = [(0,0),(1,0),(-1,0),(-1,1),(-1,-1),(0,1), (0,-1)]

def countNeighbours(coord,tiles):
    neighbours = []
    if coord[1]&1 == 0: 
        neighbours = evenNeighbours[1:]
    else:
        neighbours = oddNeighbours[1:]
    b = 0
    for n in neighbours:
        nCoord = (coord[0] + n[0], coord[1] + n[1])
        if nCoord in tiles.keys():
            if tiles[nCoord]:
                b = b+1
    return b

#print(tiles)

for day in range(1,101):
    tempTiles = {}
    for tileCoord in tiles:
        neighbours = []
        if tileCoord[1]&1 == 0: 
            neighbours = evenNeighbours
        else:
            neighbours = oddNeighbours
        for n in neighbours:
            nCoord = (tileCoord[0] + n[0], tileCoord[1] + n[1])
            if nCoord not in tempTiles.keys():
                b = countNeighbours(nCoord,tiles)
                t = False
                if nCoord in tiles.keys():
                    t = tiles[nCoord]
                
                if t and (b == 0 or b > 2):
                    # tempTiles[nCoord] = False
                    pass
                elif not t and b == 2:
                    tempTiles[nCoord] = True
                elif t:
                    tempTiles[nCoord] = True

                #print(tileCoord,nCoord,b,t,tempTiles[nCoord])

    tiles = tempTiles
print(day, tileCount(tiles))
