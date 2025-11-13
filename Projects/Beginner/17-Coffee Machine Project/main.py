class CoffeeMachine:
    def __init__(self, resources):
        self.MENU = {
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
        # self.resources = {
        #     "water": 300,
        #     "milk": 200,
        #     "coffee": 100,
        # }
        self.resources = resources
        self.profit = 0
        self.is_on = True

    @staticmethod
    def welcome():
        print("☕ Welcome to the Python Coffee Machine! ☕")
        print("Type 'report' to see resources, or 'off' to shut down.\n")

    def report(self):
        """Print the current resources and profit report."""
        print("\n--- Machine Report ---")
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.profit:.2f}\n")

    def make_coffee(self, drink_name, order_ingredients):
        """Make coffee and subtract from resources"""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}\nEnjoy!☕")


    def is_resource_sufficient(self, ingredients):
        """Return false if ingredients are more than resources"""
        for item in ingredients:
            if ingredients[item] > self.resources[item]:
                print(f"Sorry there's not enough {item}")
                return False
        return True

    @staticmethod
    def process_coins():
        """return the total payment"""
        print("Please insert coins.")
        quarters = int(input("How many Quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = float((.25 * quarters) + (.10 * dimes) + (.05 * nickles) + (.01 * pennies))
        return total



    def is_transaction_successful(self, money_received, drink_cost):
        """return True if the money received is more than the drink cost, then give change, and add to profit"""
        if money_received >= drink_cost:
            change = money_received - drink_cost
            print(f"Here is your change: ${change:.2f}")
            self.profit += drink_cost
            return True
        else:
            print(f"Sorry that's not enough money. Money refunded. ${money_received}")
            return False

    def run(self):
        self.welcome()
        while self.is_on:
            choice = input("What would you like? (espresso/latte/cappuccino):").lower()
            if choice == "off":
                print("Turning off...👋")
                self.is_on = False
            elif choice == "report":
                self.report()
            elif choice in self.MENU:
                drink = self.MENU[choice]
                # if resource are sufficient then ask for payment
                if self.is_resource_sufficient(drink["ingredients"]):
                    payment = self.process_coins()
                    #if enough money then make coffee
                    if self.is_transaction_successful(payment,drink["cost"]):
                        self.make_coffee(choice, drink["ingredients"])
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    water = int(input("Enter starting water amount (ml): "))
    milk = int(input("Enter starting milk amount (ml): "))
    coffee = int(input("Enter starting coffee amount (g): "))

    user_resources = {"water": water,
        "milk": milk,
        "coffee": coffee
                      }
    machine = CoffeeMachine(user_resources)
    machine.run()



