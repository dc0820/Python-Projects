from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
register = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    print("☕ Welcome to the Python Coffee Machine! ☕")
    options = menu.get_items()
    choice = input(f"What would you like? {options}:\n").lower()
    if choice == "off":
        print("Turning off...👋")
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        register.report()
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and register.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    else:
        print("Invalid choice. Please select a valid option.")
    menu.