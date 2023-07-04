from MemoryGame import play as play_memory
from GuessGame import play as play_guess
from CurrencyRouletteGame import play as play_rolette
from Score import add_score
def welcome():
    name = input("Please enter your name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


def load_game():
    print("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n2. Guess Game - guess a number and see if you chose like the computer.\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    choose_correct = False
    user_input = input("Please Enter your choice: ")
    difficulty = 0
    # Why using while loop? In aim that the user wil have the option to "wrong" many times
    # he wants and still the program won't stop until he wil make the right choice

    while not choose_correct:
        if user_input.isnumeric():
            if int(user_input) < 1 or int(user_input) > 3:
                print("Please enter a number between 1 - 3!")
                user_input = input("Please Enter your choice: ")
            else:
                choose_correct = True
                difficulty = choose_difficulty()
        else:
            print("Please enter a number and not a string!")
            user_input = input("Please Enter your choice: ")

    user_input = int(user_input)
    if user_input == 1:
        res = play_memory(difficulty)
        if res:
            score = add_score(difficulty)
        else:
            BAD_RETURN_CODE = -1


    elif user_input == 2 :
        res = play_guess(difficulty)
        if res:
            score = add_score(difficulty)
        else:
            BAD_RETURN_CODE = -1

    elif user_input == 3 :
        res = play_rolette(difficulty)
        if res:
            score = add_score(difficulty)
        else:
            BAD_RETURN_CODE = -1


# def play_again():
#     print("you want to play again? (y/n)")
#     user_input = input("Please Enter your choice: ")
#     if user_input == "y":
#         load_game()
#     else:
#         print("Thank you for playing, Goodbye!")
#         return



def choose_difficulty():
    print("Please choose game difficulty from 1 to 5, where 1 is the easiest and 5 is the hardest")
    choose_correct = False
    user_input = input("Please Enter your choice: ")

    while not choose_correct:
        if user_input.isnumeric():
            if int(user_input) < 1 or int(user_input) > 5:
                print("Please enter a number between 1 - 5!")
                user_input = input("Please Enter your choice: ")
            else:
                choose_correct = True
                return int(user_input)
        else:
            print("Please enter a number and not a string!")
            user_input = input("Please Enter your choice: ")



