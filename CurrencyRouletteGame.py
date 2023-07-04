from currency_converter import CurrencyConverter
import random


def get_money_interval(difficulty,random_num):
    c = CurrencyConverter()
    currency_ils = c.convert(random_num, 'USD', 'ILS')
    min = currency_ils - (5 - difficulty)
    max = currency_ils + (5 - difficulty)
    return (min, max)


def get_guess_from_user(random_num):
    user_input = input(f"Please guess the value of {random_num} USD in ILS: ")
    choose_correct = False
    while not choose_correct:
        if user_input.isnumeric():
            choose_correct = True
            return int(user_input)
        else:
            print("Please enter a number and not a string!")
            user_input = input("Please Enter your choice: ")

def play(difficulty):
    random_num = random.randint(1, 101)
    min, max = get_money_interval(difficulty, random_num)
    user_guess = get_guess_from_user(random_num)
    if user_guess >= min and user_guess <= max:
        print("You won!")
        return True
    else:
        print("You lost!")
        return False

