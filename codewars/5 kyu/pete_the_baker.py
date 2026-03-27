def cakes(recipe: dict[str, int], available: dict[str, int]) -> int:
    return min(available.get(ingredient, 0) // recipe[ingredient] for ingredient in recipe.keys())