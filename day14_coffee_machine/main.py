menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resource_units = ['ml', 'ml', 'g']

def resource_report():
    for index, (key, value) in enumerate(resources.items()):
        print(f"{key.capitalize()}: {value} {resource_units[index]}")
    print(f"Money: ${money}")

def check_resources(drink):
    if drink in ['espresso','latte','cappucchino']:
        for ingredient in resources:
            if resources[ingredient] < menu[drink]['ingredients'][ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                return
    else:
        print('Invalid drink selection.')

def process_coins(drink):
    print("Please insert coins.")
    n_quarters = int(input("How many quarters?: "))
    n_dimes = int(input("How many dimes?: "))
    n_nickles = int(input("How many nickles?: "))
    n_pennies = int(input("How many pennies?: "))
    coins_value = (n_quarters * 0.25) + (n_dimes * 0.10) + (n_nickles * 0.05) + (n_pennies * 0.01)
    drink_cost = menu[drink]['cost']
    if coins_value < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return
    elif coins_value > drink_cost:
        print(f"Here is ${round(coins_value - drink_cost,2)} in change.")
    global money
    money += drink_cost

def make_coffee(drink, current_resources=resources):
    for resource in current_resources:
        current_resources[resource] -= menu[drink]['ingredients'][resource]
    print(f"Here is your {drink}. Enjoy!")

machine_on = True
while machine_on:
    order = input("What would you like? (espresso/latte/cappucchino): ")
    if order == 'off':
        machine_on = False
    elif order == 'report':
        resource_report()
    else:
        check_resources(order)
        process_coins(order)
        make_coffee(order)


