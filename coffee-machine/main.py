from menu import MENU
from menu import resources

def print_report():
    for resource in resources:
        print(f"{resource} : {resources[resource]}ml")

def process_prompt(prompt):
    sufficent_ingredients = True
    if prompt == 'espresso' or prompt == 'latte' or prompt == 'cappuccino':

        for ingredient in MENU[prompt]["ingredients"]:
            if MENU[prompt]["ingredients"][ingredient] > resources[ingredient]:
                sufficent_ingredients = False
                print(f"Insufficient {ingredient}")
                break
        if sufficent_ingredients:
            money = float(input(f"Please insert {MENU[prompt]['cost']}"))
            if money >= MENU[prompt]['cost']:
                print(f"Change: {money - MENU[prompt]['cost']}")
                for ingredient in MENU[prompt]["ingredients"]:
                    resources[ingredient] -= MENU[prompt]["ingredients"][ingredient]
                resources['money'] += MENU[prompt]["cost"]
                return True
            else:
                print(f"Not enough coins, order cancelled\n")
                return False
        else:
            return True
    elif prompt == 'report':
        print_report()
        return True
    elif prompt == 'off':
        print("Turning off...")
        return False

continue_order = True
while continue_order:
    coffee_order = input("What would you like?\nespresso $5\nlatte $15\ncappuccino $10\n")
    continue_order = process_prompt(coffee_order)
