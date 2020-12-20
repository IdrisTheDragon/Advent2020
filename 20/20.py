import numpy as np


class Tile:
    def __init__(self, id, tileData):
        self.id = id
        self.tileData = np.array(tileData)
        self.neighbours = []
        #print(self.tileData)
        self.borders = [self.tileData[0],self.tileData[-1],self.tileData[:,-1],self.tileData[:,0]] # grab borders
        self.tileData = self.tileData[1:-1,1:-1] # trim off borders

    def __repr__(self):
        return "{0}".format(self.id)

    def __str__(self):
        return "{0}".format(self.id)

    def setNeighbour(self, tile1):
        if tile1 not in self.neighbours:
            self.neighbours.append(tile1)
            tile1.neighbours.append(self)

    def countHash(self):
        count = 0
        for x in self.tileData:
            for y in x:
                if y =='#':
                    count = count+1
        return count


    def checkIfNeighbour(self, tile1):
        for b in self.borders:
            for bt in tile1.borders:
                if np.array_equal(b, bt) or np.array_equal(b, bt[::-1]):
                    return True
        return False



#f = open("example.txt", "r")
#f = open("example1.txt", "r")
f = open("input.txt", "r")
l = []
id = 0
tileData = []
for x in f:
    if 'Tile' in x:
        x = x.split()
        id = int(x[1][:-1])
    elif x == '\n':
        l.append(Tile(id,tileData))
        tileData = []
    else:
        tileData.append(list(x[:-1]))

#print(l)

for tile in l:
    for tile1 in l:
        if tile == tile1:
            continue
        if tile.checkIfNeighbour(tile1):
            tile.setNeighbour(tile1)

sum = 1
for x in l:
    #print(x.neighbours)
    if len(x.neighbours) == 2:
        sum = sum *x.id
print(sum)

count = 0
for x in l:
    count = count + x.countHash()

print(count)
# a little brute force..
# for size of grid compared to example maybe 15 monsters?
# more than 15 monsters..
# more than 20 monsters..
print(count - (15*25))
    
