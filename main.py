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
money = 0


def shut_down():
    print("Shutting off the Coffee Maker now.")


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


# TODO: Display the cost of the selection and confirm
# TODO: Process coins to pay for the selection and return change
# TODO: Verify if the transaction was successful
# TODO: Process beverage


selection = order_drink()
if selection == "off":
    shut_down()
elif selection == "report":
    print_report()
else:
    enough_resources = check_resources(selection)
    if not enough_resources:
        print("Sorry, we don't have enough resources to make that selection.")