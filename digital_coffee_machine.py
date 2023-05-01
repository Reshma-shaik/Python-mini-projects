"""
This Python program is about ordering the coffee digitally.
"""

#  Allocate Resources(This program can make 1 espresso and 1 latte or 1 espresso and 1 cappuccino or 5 espresso coffee
#  with the available ingredients)
ingredients = {
    "milk": 200,  # in ml
    "water": 300,  # in ml
    "coffee_powder": 100  # in grams
}
# Resources required for the type of Coffee
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee_powder": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee_powder": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee_powder": 24,
        },
        "cost": 3.0,
    }
}


def process_entered_coins() -> int:
    """
    description: process the digitally entered coins and calculates the amount.
    returns: calculated amount.
    """
    coins = ["quarters", "dimes", "nickel", "pennies"]
    entered_coins = []
    for coin in coins:
        _amount = input(f"how many {coin}?: ")
        _amount = 0 if not _amount or not _amount.isnumeric() else int(_amount)
        entered_coins.append(_amount)
    return sum([entered_coins[0] * 0.25 + entered_coins[1] * 0.10 + entered_coins[2] * 0.05 + entered_coins[3] * 0.01])


def check_ingredients(available_ingredients: dict, coffee: dict) -> bool:
    """
    description: checks and updates the ingredients that are available to make the coffee.
    returns: boolean value.
    """
    for ingredient in coffee["ingredients"]:
        if available_ingredients[ingredient] <= coffee["ingredients"][ingredient]:
            return False
        else:
            available_ingredients[ingredient] -= coffee["ingredients"][ingredient]
    return True


def check_balance(amount: float, cost: float) -> float:
    """
        Deducts the amount that is paid and returns balance if any else returns the amount
    """
    if amount > cost:
        return round(amount-cost, 2)
    else:
        return amount


print("Hello!\n")

while True:
    # Get the input from user
    display_options = "I make following types of Coffee:\n What would you like to have\n" \
                      " 1. espresso\n 2. latte \n 3. cappuccino\n"
    choice = input(display_options)
    # Stop the Digital Coffee Machine
    if choice == "off":
        break
    # Display the available ingredients
    elif choice == "report":
        print(f"Available resources \n Water: {ingredients['water']}\n Milk: {ingredients['milk']}"
              f" \n Coffee: {ingredients['coffee_powder']}")
    # check for the option that user chose if available or not
    elif choice not in MENU or not choice:
        print("\n\n!!!Wrong input!!!\nPlease select from the below options")
        continue
    # Process amount and make coffee based on available ingredients
    elif choice in MENU:
        ordered_item = check_ingredients(ingredients, MENU[choice])
        if not ordered_item:
            print("Sorry! There is no available ingredients to make this coffee")
        else:
            cost = MENU[choice]["cost"]
            amount = process_entered_coins()
            if amount >= cost:
                if amount > cost:
                    print("Balance amount: ", check_balance(amount, cost))
                print("Here is your ordered coffee ☕️. \nThank You for ordering!")
            else:
                print("Sorry! the amount you gave is not enough")
