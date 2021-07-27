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


def shut_down():
    print("Shutting off the Coffee Maker now.")
    return "shut_down"


def print_report(money_collected):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money_collected:.2f}")


def order_drink():
    menu_choice = input("What would you like to order? "
                        "(Type 'E' for Espresso, 'L' for Latte, or 'C' for Cappuccino): ").lower()
    if menu_choice == "e":
        return "espresso"
    elif menu_choice == "l":
        return "latte"
    elif menu_choice == "c":
        return "cappuccino"
    else:
        return menu_choice


# TODO: Verify if there are enough resources to process the selection. Determine which resource(s) we are short on


def check_resources(drink_selection):
    """Takes a drink_selection as input and returns True if there are sufficient resources, otherwise False"""
    for key in MENU[drink_selection]["ingredients"]:
        if MENU[drink_selection]["ingredients"][key] > resources[key]:
            return False
        else:
            return True


def payment_processing(beverage):
    """Takes the selected beverage as input and returns the processed payment amount or cost if succesful"""
    coins = {}
    total_payment_collected = 0.00
    cost = MENU[beverage]["cost"]

    print("Please insert coins.")
    coins["quarters"] = input("How many quarters?: ")
    coins["dimes"] = input("How many dimes?: ")
    coins["nickels"] = input("How many nickels?: ")
    coins["pennies"] = input("How many pennies?: ")
    for key in coins:
        if coins[key] == "":
            coins[key] = 0
        coins[key] = int(coins[key])
    total_money_collected = coins["quarters"] * .25 + coins["dimes"] * .10 + coins["nickels"] * .05 + coins["pennies"] * .01
    if cost > total_money_collected:
        print("Sorry that's not enough money.  Money refunded.")
        return False
    else:
        change = total_money_collected - cost
        print(f"Here is {change:.2f} in change.")
        print(f"Enjoy your {beverage}, have a great day!")
        return cost


def run_coffee_machine():
    print(cup)
    turn_off = ""
    money = 0.00
    while turn_off != "shut_down":
        selection = order_drink()
        if selection == "off":
            turn_off = shut_down()
        elif selection == "report":
            print_report(money)
        else:
            enough_resources = check_resources(selection)
            if not enough_resources:
                print("Sorry, we don't have enough resources to make that selection.")
            else:
                transaction_amount = payment_processing(selection)
                if transaction_amount:
                    money += transaction_amount
    return money


run_coffee_machine()




