from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == 'off':
        machine_on = False
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink_order = menu.find_drink((order))
        if coffee_maker.is_resource_sufficient(drink_order) == True:
            money_machine.make_payment(drink_order.cost)
            coffee_maker.make_coffee(drink_order)


