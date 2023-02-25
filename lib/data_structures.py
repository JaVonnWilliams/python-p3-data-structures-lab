spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food_name["name"] for food_name in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [hot_food for hot_food in spicy_foods if hot_food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for foods in spicy_foods:
        print(f'{foods["name"]} ({foods["cuisine"]}) | Heat Level: {"🌶" * foods["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for foods in spicy_foods:
        if foods["cuisine"] == cuisine:
            return foods

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    return sum([foods["heat_level"] for foods in spicy_foods]) / len(spicy_foods) 

def create_spicy_food(spicy_foods, new_spicy_food):
     spicy_foods.append(new_spicy_food)
     return spicy_foods
