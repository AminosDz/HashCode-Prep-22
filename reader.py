

def read(filename):

    f = open(filename)

    ingredients = []
    clients = []

    C = int(f.readline().strip())

    for client in range(C):
        line = f.readline().strip().split()
        L, l_ingredients = int(line[0]), line[1:]
        
        like_ingredients = []
        for l in range(L):
            like_ingredients.append(index_ingredient(ingredients, l_ingredients[l]))

        line = f.readline().strip().split()
        D, d_ingredients = int(line[0]), line[1:]

        dis_ingredients = []
        for d in range(D):
            dis_ingredients.append(index_ingredient(ingredients, d_ingredients[d]))

        clients.append((like_ingredients, dis_ingredients))

    return clients, ingredients
    
    
def index_ingredient(ingredients, ingredient):
    if ingredient in ingredients:
        return ingredients.index(ingredient)

    ingredients.append(ingredient)
    return len(ingredients)-1
