from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Welcome to the Coffee Machine!")

while True:
    print("Please select a drink from the menu:")
    print(menu.get_items())
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    drink = menu.find_drink(choice)

    if drink is None:
        print("Invalid selection. Please try again.")
        continue

    if not coffee_maker.is_resource_sufficient(drink):
        print("Sorry, we cannot make that drink due to insufficient resources.")
        continue

    if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
        money_machine.report()
        coffee_maker.report()
    else:
        print("Insufficient money. Please try again.")

    another_order = input("Do you want to order another drink? (yes/no): ").lower()
    if another_order != "yes":
        break

print("Thank you for using the Coffee Machine. Have a great day!")
print("Final Report:")
money_machine.report()
coffee_maker.report()
print(f"Total profit: ${money_machine.profit:.2f}")