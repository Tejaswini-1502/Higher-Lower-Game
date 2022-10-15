from art import logo, vs
from game_data import data
import random
from replit import clear

score = 0  #intial score is set to zero
"""Format the account data into printable format"""


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}."


"""Use an if statement, to check if the user is correct"""


def check_answer(guess, a_followers, b_followers):
    if guess == 'a':
        if a_followers > b_followers:
            return True
        else:
            return False
    else:
        if b_followers > a_followers:
            return True
        else:
            return False


#display art
print(logo)
continue_game = True

accountB = random.choice(data)

while continue_game:

    #generate a random account from the given data
    accountA = accountB
    accountB = random.choice(data)
    while accountA == accountB:
        accountB = random.choice(data)

    #Format the account data
    print(f"Compare A: {format_data(accountA)}")
    print(vs)
    print(f"Against B: {format_data(accountB)}")

    #Ask user to guess who among the above two has highest instagram followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Check if the answer given by the user is right or wrong
    ## Get follower count of each account

    a_follower_count = accountA["follower_count"]
    b_follower_count = accountB["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Clearing the screen between the rounds.
    clear()
    print(logo)
    #Give user the feedback about their guess
    #Also keep track of the current score

    if (is_correct):
        score += 1
        print(f"You're right! Current Score: {score}")

    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        continue_game = False

    #If the user gets it right, current score is increamented by 1 and the game is repeated and making account B move from second to first position else the game ends here just diaplying the current score
