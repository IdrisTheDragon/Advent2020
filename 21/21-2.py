

#f = open("example.txt", "r")

f = open("input.txt", "r")
ingredients = set()
ingredientsCount = {}
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

    ingredients = ingredients.union(set(ingredient))
    for i in ingredient:
        if i not in ingredientsCount:
            ingredientsCount[i] = 1
        else:
            ingredientsCount[i] = ingredientsCount[i] + 1

    for a in allergen:
        if a not in allergens:
            allergens[a] = set(ingredient)
        else:
            allergens[a] = allergens[a].intersection(set(ingredient))

allergenIngredients = set().union(*allergens.values())

notAllegensIngredients = ingredients.symmetric_difference(allergenIngredients)
#print(notAllegensIngredients)

sum = 0
for i in notAllegensIngredients:
    sum = sum + ingredientsCount[i]
print(sum)

print(allergens)

completed_allergens = {}
completed_ingredients = set()

finished = False
while not finished:
    finished = True
    for a,i in allergens.items():
        diff = i-completed_ingredients
        #print(diff)
        if len(diff) == 1:
            finished =False
            fi = diff.pop()
            completed_allergens[a] = fi
            completed_ingredients.add(fi)
            
        
print(completed_allergens)
sorted_allergens = sorted(completed_allergens.items(), key=lambda x: x[0], reverse=False)

result = ''
for x in sorted_allergens:
    result = result + x[1] + ','
print(result[:-1])
            