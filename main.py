from art import cup

MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
print(cup)
money = 0.00


def shut_down():
    print("Shutting off the Coffee Maker now.")
    return


def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money:.2f}")


def order_drink():
    menu_choice = input("What would you like to order? "
                        "(Type 'E' for Espresso, 'L' for Latte, or 'C' for Cappuccino): ").lower()
    if menu_choice == "e":
        return MENU["espresso"]
    elif menu_choice == "l":
        return MENU["latte"]
    elif menu_choice == "c":
        return MENU["cappuccino"]
    else:
        return menu_choice


# TODO: Verify if there are enough resources to process the selection. Determine which resource(s) we are short on


def check_resources(drink_selection):
    """Takes a drink_selection as input and returns True if there are sufficient resources, otherwise False"""
    for key in drink_selection["ingredients"]:
        if drink_selection["ingredients"][key] > resources[key]:
            return False
        else:
            return True


# TODO: Process coins to pay for the selection and return change


def payment_processing(beverage):
    """Takes the selected beverage as input and returns the processed payment amount or cost if succesful"""
    coins = {}
    total_money_collected = 0.00
    cost = beverage["cost"]

    print("Please insert coins.")
    coins["quarters"] = input("How many quarters?: ")
    coins["dimes"] = input("How many dimes?: ")
    coins["nickels"] = input("How many nickels?: ")
    coins["pennies"] = input("How many pennies?: ")
    # Loop allows for user to just hit return if they don't have that type of coin and have it equate to 0
    for key in coins:
        if coins[key] == "":
            coins[key] = 0
        coins[key] = int(coins[key])
    total_money_collected = coins["quarters"] * .25 + coins["dimes"] * .10 + coins["nickels"] * .05 + coins["pennies"] * .01
    # print(total_money_collected)
    if cost > total_money_collected:
        print("Sorry that's not enough money.  Money refunded")
        return False
    else:
        print(f"Here is your {next(iter(beverage))}")
        return cost


# TODO: Verify if the transaction was successful
# TODO: Process beverage


def run_coffee_machine():
    selection = order_drink()
    if selection == "off":
        shut_down()
    elif selection == "report":
        print_report()
    else:
        enough_resources = check_resources(selection)
        if not enough_resources:
            print("Sorry, we don't have enough resources to make that selection.")
        money_collected = payment_processing(selection)
        if not money_collected:
            run_coffee_machine()
        else:
            return money_collected


money = run_coffee_machine()
print(money)



