from menu import MENU

# Start of Function section


def userChoice():
    """This is a function which checks what user entered to the machine.
    And returns the input string."""

    UserChoice = input("What would you like? (espresso/latte/cappuccino): ")

    while (UserChoice != "espresso") and (UserChoice != "latte") and (UserChoice != "cappuccino") and (UserChoice != "report") and (UserChoice != "off"):
        UserChoice = input(
            "What would you like? (espresso/latte/cappuccino): ")

    return UserChoice


def coinChecker(Coin, TypeOFCoin):
    """This function is a support function to userCoins() function,
    Witch checks if the input of the user is valid for the system.
    And returns the amount of the coin."""

    Coin = input(f"How many {TypeOFCoin}?: ")

    while not Coin.isdigit():
        Coin = input(f"How many {TypeOFCoin}?: ")

    return int(Coin)


def userCoins():
    """This function returns a tuple of the amount of Coins the the user inserted into
    the machine."""
    Quarters = 0
    Dimes = 0
    Nickles = 0
    Pennies = 0
    print("Please insert coins.")
    Quarters = coinChecker(Quarters, "Quarters")
    Dimes = coinChecker(Dimes, "Dimes")
    Nickles = coinChecker(Nickles, "Nickles")
    Pennies = coinChecker(Pennies, "Pennies")

    return Quarters, Dimes, Nickles, Pennies


def suppliesCheck(MENU, UserChoice, Water, Milk, Coffee):
    """This function checks if the machine has sufficient amount of each of the
    supplies and returns False when it finds that a supply is not sufficient for the current
    picked item."""

    for ingredient in MENU[UserChoice]["ingredients"]:
        if ((Water - (MENU[UserChoice]['ingredients'][ingredient])) < 0):
            print(f"Sorry there is not enough {ingredient}")
            return False
        elif ((Milk - (MENU[UserChoice]['ingredients'][ingredient])) < 0):
            print(f"Sorry there is not enough {ingredient}")
            return False
        elif ((Coffee - (MENU[UserChoice]['ingredients'][ingredient])) < 0):
            print(f"Sorry there is not enough {ingredient}")
            return False

    return True


def coffeeMaking(UserChoice, Menu, Water, Milk, Coffee):
    """This function creates the coffee and removes the amount of each resource
    depending what the user choose"""

    for ingredient in Menu[UserChoice]["ingredients"]:
        if ingredient == "water":
            Water = Water - Menu[UserChoice]["ingredients"]["water"]
        elif ingredient == "milk":
            Milk = Milk - Menu[UserChoice]["ingredients"]["milk"]
        else:
            Coffee = Coffee - Menu[UserChoice]["ingredients"]["coffee"]

    return Water, Milk, Coffee


def moneyChecking(Money, UserCoins, UserChoice, CoinValues, MENU):
    """In this function checks if the user provided sufficient amount of
    money to pay"""
    UserChange = 0
    UserMoney = 0

    for coin in UserCoins:
        for coinValue in CoinValues:
            UserMoney = UserMoney + (coin * CoinValues[coinValue])

    UserChange = change(UserMoney, MENU, UserChoice)

    if UserChange == False:
        return False
    else:
        if UserChange == 0:
            print(f"Here is you {UserChoice} ☕ Enjoy!")
            return Money + MENU[UserChoice]["cost"]
        else:
            print(
                f"Here is ${UserChange} in change\nHere is you {UserChoice} ☕ Enjoy!")
            return Money + MENU[UserChoice]["cost"]


def change(UserMoney, MENU, UserChoice):
    """In this function checks if the user needs any change back"""

    UserChange = 0
    for coffeeType in MENU:
        if (coffeeType == UserChoice):
            if ((MENU[coffeeType]["cost"]) < UserMoney):
                UserChange = UserMoney - (MENU[coffeeType]["cost"])
                return UserChange
            elif ((MENU[coffeeType]["cost"]) > UserMoney):
                return False
            else:
                return 0


def adminOutput(Water, Milk, Coffee, Money):

    print(
        f"Water: {Water}ml\nMilk: {Milk}ml\nCoffee: {Coffee}g\nMoney: ${Money}")


def adminCheck(AdminValues):
    """In this function check the credential of admin"""

    print("You have two chances")
    Username = input("Username: ")
    Password = input("Password: ")

    for value in AdminValues:
        if (AdminValues[value] == Username) and (AdminValues[value] == Password):
            print(f"{value} Ok")
        else:
            return False
    return True


    # End of Function section
Water = 600
Milk = 600
Coffee = 600
MachineMoney = 0
MachineWorks = True

# Coins
CoinValues = {"Quarters": 0.25,
              "Dimes": 0.10,
              "Nickles": 0.15,
              "Pennies": 0.25}

# Admin Values
Admin = {"Username": "admin",
         "Password": "admin",
         }

while MachineWorks:
    UserChoice = userChoice()

    if (UserChoice == "off") or (UserChoice == "report"):
        if (adminCheck(Admin) == True):

            if (UserChoice == "report"):
                adminOutput(Water, Milk, Coffee, MachineMoney)
            elif (UserChoice == "off"):
                MachineWorks = False
    else:
        # espresso / latte / cappuccino
        if (suppliesCheck(MENU, UserChoice, Water, Milk, Coffee) == True):

            CheckMoney = moneyChecking(
                MachineMoney, userCoins(), UserChoice, CoinValues, MENU)
            if CheckMoney == False:
                print("Not enough money")
                continue
            else:
                Water = coffeeMaking(UserChoice, MENU, Water, Milk, Coffee)[0]
                Milk = coffeeMaking(UserChoice, MENU, Water, Milk, Coffee)[1]
                Coffee = coffeeMaking(UserChoice, MENU, Water, Milk, Coffee)[2]

                MachineMoney = MachineMoney + float(CheckMoney)
