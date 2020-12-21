
class Ingredient:
    def __init__(self,ingredient):
        self.ingredient = ingredient
        self.allergens = {}
        self.appearances = 0

    def __repr__(self):
        return "{0}  {1}".format(self.appearances, self.allergens)

    def __str__(self):
        return "{0} {1}".format(self.appearances, self.allergens)



#f = open("example.txt", "r")

f = open("input.txt", "r")
ingredients = {}
allergens = {}
for x in f:
    x=x.split('(')
    ingredient = x[0][:-1].split(' ')
    allergen = x[1][9:-2].split(' ')
    #print(ingredients,allergens)
    tempA = []
    for a in allergen:
        a = a.strip(',')
        tempA.append(a)
    allergen = tempA

    for i in ingredient:
        if i not in ingredients.keys():
            i1 = Ingredient(i)
            ingredients[i] = i1
        i1 = ingredients[i]
        i1.appearances = i1.appearances + 1
        for a in allergen:
            
            if a in i1.allergens.keys():
                i1.allergens[a] = i1.allergens[a] + 1
            else:
                i1.allergens[a] = 1 

            if a in allergens.keys():
                allergens[a] = allergens[a]+1
            else:
                allergens[a] = 1

#print(ingredients)
#print(allergens)

sorted_allergens = sorted(allergens.items(), key=lambda x: x[1], reverse=True)

completed_allergens = {}

print(sorted_allergens)

for a in sorted_allergens:
    a = a[0]
    highestProbability = 0
    seen = 0
    name = ''
    for i in ingredients.values():
        #print(a , i.allergens.keys())
        if a in i.allergens.keys():
            count = i.allergens[a]
            nH = sorted(i.allergens.items(), key=lambda x:x[1])[-1]
            if nH[1] == count:
            # print(a,i.allergens)
                if count > highestProbability:
                    highestProbability = count
                    seen = i.appearances
                    name = i.ingredient
                # elif count == highestProbability:
                #      if seen > i.appearances:
                #          highestProbability = count
                #          seen = i.appearances
                #          name = i.ingredient

    completed_allergens[a] = name
    ingredients.pop(name)
    for i in ingredients.values():
        if a in i.allergens.keys():
            i.allergens.pop(a)

print(completed_allergens)
print()
#print(ingredients)

sum = 0        
for i in ingredients.values():
    sum = sum + i.appearances
print(sum)

sorted_allergens = sorted(completed_allergens.items(), key=lambda x: x[0], reverse=False)
#print(sorted_allergens)

result = ''
for x in sorted_allergens:
    result = result + x[1] + ','
print(result[:-1])

# peanuts and eggs wrong way round.. not sure what the bug is to resolve it..