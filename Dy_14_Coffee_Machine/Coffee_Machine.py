# Initial inventory of the coffee machine
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def display_inventory():
    print(
        f"Inventory:\nWater: {water}ml\nMilk: {milk}ml\nCoffee Beans: {coffee_beans}g\nDisposable Cups: {disposable_cups}\nMoney: ${money}\n")


def take_order():
    order = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    if order == "espresso":
        make_coffee(250, 0, 16, 4, 1)
    elif order == "latte":
        make_coffee(350, 75, 20, 7, 1)
    elif order == "cappuccino":
        make_coffee(200, 100, 12, 6, 1)
    else:
        print("Invalid choice. Please choose from espresso, latte, or cappuccino.")


def make_coffee(water_needed, milk_needed, coffee_beans_needed, cost, cups_needed):
    global water, milk, coffee_beans, disposable_cups, money

    try:
        if water >= water_needed and milk >= milk_needed and coffee_beans >= coffee_beans_needed and disposable_cups >= cups_needed:
            print("Preparing your coffee...")
            water -= water_needed
            milk -= milk_needed
            coffee_beans -= coffee_beans_needed
            disposable_cups -= cups_needed
            money += cost
            print("Here's your coffee! Enjoy!")
        else:
            raise Exception("Insufficient resources to make that coffee.")
    except Exception as e:
        print(e)


def refill_machine():
    global water, milk, coffee_beans, disposable_cups
    water += int(input("Enter the amount of water to refill: "))
    milk += int(input("Enter the amount of milk to refill: "))
    coffee_beans += int(input("Enter the amount of coffee beans to refill: "))
    disposable_cups += int(input("Enter the number of disposable cups to refill: "))


def take_money():
    global money
    print(f"Taking ${money}")
    money = 0


while True:
    action = input("What would you like to do? (buy/fill/take/report/exit): ").strip().lower()

    if action == "buy":
        take_order()
    elif action == "fill":
        refill_machine()
    elif action == "take":
        take_money()
    elif action == "report":
        display_inventory()
    elif action == "exit":
        break
    else:
        print("Invalid choice. Please choose from buy, fill, take, report, or exit.")