import collections
import re

food_pattern = re.compile(r"(.*)\s\(contains\s(.*)\)")

allergens = {}
all_ingredients = collections.defaultdict(int)

with open("input.txt", "r") as input_file:
    for input_line in input_file:
        input_line = input_line.strip()
        match = food_pattern.search(input_line)
        if match is None:
            continue
        ingredients_list = match.group(1).split(" ")
        allergen_list = match.group(2).split(", ")

        print("---------------------------------")
        print("Line: {}".format(input_line))
        print("Ingredients: {}".format(ingredients_list))
        print("Allergens: {}".format(allergen_list))

        for ingredient in ingredients_list:
            all_ingredients[ingredient] += 1

        for allergen in allergen_list:
            if allergen not in allergens:
                print("Adding record for allergen {}.".format(allergen))
                allergens[allergen] = set(ingredients_list)
            else:
                print("Allergen {} exists.".format(allergen))
                allergens[allergen] &= set(ingredients_list)

# print('{:-^100}'.format(" INTERMEDIATE: "))
# print(allergens)

all_detected = False

while not all_detected:
    for allergen, ingredients in allergens.items():
        if len(ingredients) == 1:
            for allergen2 in allergens.keys():
                if allergen2 != allergen:
                    allergens[allergen2] = allergens[allergen2] - ingredients

    all_detected = True
    for allergen, ingredients in allergens.items():
        if len(ingredients) != 1:
            all_detected = False

print('{:-^100}'.format(" ALLERGENS: "))
print(allergens)

allergic_ingredients = []
for allergen in sorted(allergens.keys()):
    allergic_ingredients.append(list(allergens[allergen]).pop())

print(','.join(allergic_ingredients))
