############### Blackjack Project #####################
import random
from replit import clear
from art import logo

############# Start of Function Section #############


def initialHand(cards):
    """This function use to create an initial hand for
    the user and computer. It has only one parameter cards
    and returns the hand list with two random elements"""

    hand = []
    for InitialCards in range(0, 2):
        hand.append(random.choice(cards))

    return hand


def addCards(cards, hand):
    """This function just gives one more card."""

    hand.append(random.choice(cards))
    return hand


def handCount(hand):
    """A function witch take the hand as variable
    and returns the count of this hand"""

    count = 0
    for card in hand:
        count += card

    return count


def userCardChoice():
    """Ask the user if wants one more card"""

    UserChoice = input("Do you want another card ? ")

    while (UserChoice != 'y') and (UserChoice != 'n'):
        UserChoice = input("Do you want another card ? ")

    return UserChoice


def userNewGameChoice():
    """Ask the user if wants to play one more game"""

    UserChoice = input("Do you want to play one more game ? ")

    while (UserChoice != 'y') and (UserChoice != 'n'):
        UserChoice = input("Do you want to play one more game ? ")

    if UserChoice == 'y':
        return False
    else:
        clear()
        print("Buy 🫡  👋!!")
        return True


def userHand(cards, UserHand):
    """This function just initialize the first hand of the user.
    And then give one more card to the user each time"""

    Count = 0

    if UserHand == []:
        UserHand = initialHand(cards)
        Count = handCount(UserHand)

        if Count > 21:
            for card in range(len(UserHand)):
                if UserHand[card] == 11:
                    UserHand[card] = 11
                    Count = handCount(UserHand)

        print("############ User Initial Hand ############")
        print(
            f"The initial user hand ♣️ is: {UserHand}\nAnd the cards count is: {Count}\n")
        return UserHand

    UserHand = addCards(cards, UserHand)
    Count = handCount(UserHand)
    if Count > 21:
        print("Is > 21")
        for card in range(len(UserHand)):
            if UserHand[card] == 11:
                print("Found 11")
                UserHand[card] = 1
                Count = handCount(UserHand)
    print("\n############ User Next Hand ############")
    print(
        f"The user's hand ♣️ is: {UserHand}\nAnd the cards count is: {Count}\n")
    return UserHand


def computerHand(cards, ComputerHand):
    """This function just initialize the first hand of the computer / dealer.
    And then gives one more card to the computer / dealer each time"""

    Count = 0

    if ComputerHand == []:
        ComputerHand = initialHand(cards)
        Count = handCount(ComputerHand)
        if Count > 21:
            for card in range(len(ComputerHand)):
                if ComputerHand[card] == 11:
                    print("Found 11")
                    ComputerHand[card] = 1
                    Count = handCount(ComputerHand)
        print("\n############ Computer Initial Hand ############")
        print(f"The initial computer hand ♣️ is: _ {ComputerHand[1]}\n")
        return ComputerHand

    ComputerHand = addCards(cards, ComputerHand)
    Count = handCount(ComputerHand)
    if Count > 21:
        for card in range(len(ComputerHand)):
            if ComputerHand[card] == 11:
                print("Found 11")
                ComputerHand[card] = 1
                Count = handCount(ComputerHand)
    print("############ Computer Next Hand ############")
    print(
        f"The computer's hand ♣️ is: {ComputerHand}\nAnd the cards count is: {Count}\n")
    return ComputerHand


def compareHands(UserHandCount, ComputerHandCount, UserCash, UserBet):
    """A function which takes the two hands of the User and Computer 
    and compare them returning the outcome"""

    if (UserHandCount == ComputerHandCount):
        UserBet = round(UserBet / 2)
        UserCash = UserCash + UserBet
        print(
            f"\nIt's a draw 😐!!\nUser hand count is: {UserHandCount}\nDealer's hand count is: {ComputerHandCount}\nUser cash 💰 is: {UserCash}\n")
        return UserCash
    elif (UserHandCount > ComputerHandCount):
        UserCash = UserCash + UserBet
        print(
            f"\nYou Won 🤩!!\nUser hand count is: {UserHandCount}\nDealer's hand count is: {ComputerHandCount}\nUser cash 💰 is: {UserCash}\n")
        return UserCash
    else:
        UserCash = UserCash - UserBet
        print(
            f"\nYou Lost 😭!!\nUser hand count is: {UserHandCount}\nDealer's hand count is: {ComputerHandCount}\nUser cash 💰 is: {UserCash}\n")
        return UserCash


def askUserToBet(UserCash):

    UserBet = int(input(
        f"What is your bet? Your balance is: {UserCash}. You are able to bet lower than your budget or equal "))
    while UserBet > UserCash:
        UserBet = int(input(
            f"fWhat is your bet? Your balance is: {UserCash}. You are able to bet lower than your budget or eaqual "))

    return UserBet


############# End of Function Section #############
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
UserHand = []
ComputerHand = []
ComputerHandCount = 0
UserHandCount = 0
GameEnds = False
UserChoice = 'y'
UserBet = 0
UserCash = 10

while GameEnds == False:

    print(logo)
    UserBet = askUserToBet(UserCash=UserCash)

    ComputerHand = computerHand(cards, ComputerHand)
    ComputerHandCount = handCount(ComputerHand)

    while (UserChoice != 'n'):
        UserHand = userHand(cards, UserHand)
        UserHandCount = handCount(UserHand)
        print(UserHand)
        if UserHandCount <= 21:
            UserChoice = userCardChoice()
        else:
            print(f'\nYou lost 😭 !!\nYor card count is: {UserHandCount}')
            UserCash = UserCash - UserBet
            print(f"Your new balance 💸 is: {UserCash}\n")
            GameEnds = True
            break

    if GameEnds != True:
        print("\n############## Computer's Round ##############")
        print(
            f'The computer\'s initial hand ♣️ is: {ComputerHand}\nHand count: {ComputerHandCount}\n')
        while ComputerHandCount < 17:
            if ComputerHandCount >= 17:
                break
            ComputerHand = computerHand(cards=cards, ComputerHand=ComputerHand)
            ComputerHandCount = handCount(ComputerHand)
        if ComputerHandCount > 21:
            print("You won 🤩!!")
            UserCash = UserCash + UserBet
            print(f"Your new balance 💰 is: {UserCash}\n")
            GameEnds = True
        else:
            UserCash = (compareHands(UserHandCount=UserHandCount,
                        ComputerHandCount=ComputerHandCount, UserCash=UserCash, UserBet=UserBet))
            GameEnds = True

    if (UserCash > 0):
        GameEnds = userNewGameChoice()
        if (GameEnds == False):
            clear()
            UserHand = []
            ComputerHand = []
            ComputerHandCount = 0
            UserHandCount = 0
            UserChoice = 'y'
    else:
        print("\nYou don't have sufficient money to continue to play 😭.")
