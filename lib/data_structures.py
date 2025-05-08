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

    return [food["name"] for food in spicy_foods]
    pass
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return[item for item in spicy_foods if item["heat_level"] > 5]
    pass
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for spicy in spicy_foods:
        print (f"{spicy['name']} ({spicy['cuisine']}) | Heat Level: {'🌶' * spicy['heat_level']}")

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if cuisine == item["cuisine"]:
            return item

   

print (get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    for spicy in spicy_foods:
        if spicy["heat_level"] > 5:
            print (f"{spicy['name']} ({spicy['cuisine']}) | Heat Level: {'🌶' * spicy['heat_level']}")
    pass

print_spiciest_foods(spicy_foods)
def get_average_heat_level(spicy_foods):
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods) 
        
    pass
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass

print(create_spicy_food(spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }))
