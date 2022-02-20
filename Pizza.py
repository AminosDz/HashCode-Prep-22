class Pizza:
    def __init__(self, ingredients = set()) -> None:
        self.ingredients = ingredients
    
    def add_ingredient(self,ing):
        self.ingredients.add(ing)
    
    def remove_ingredient(self,ing):
        self.ingredients.remove(ing)

    def write_sol(self, path):
        len_str = f'{len(self.ingredients)} '
        ing_str = " ".join(self.ingredients)

        out_str = len_str + ing_str

        f = open(path, "w")
        f.write(out_str)
        f.close