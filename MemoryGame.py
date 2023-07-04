import random
import sys
import time
import os

def generate_sequence(difficulty):
    lst = []
    for i in range(difficulty):
        lst.append(random.randint(1, 101))
    return lst

def get_list_from_user(difficulty):
    choose_correct = False
    lst = []
    user_input = input("Please Enter your choice: ")
    counter = 1
    while not choose_correct :
        while counter <= difficulty:
            if user_input.isnumeric():
                if int(user_input) < 1 or int(user_input) > 101:
                    print(f"Please enter a number between 1 - 101!")
                    user_input = input("Please Enter your choice: ")
                else:
                    lst.append(int(user_input))
                    choose_correct = True
                    counter += 1
                    if counter <= difficulty:
                        user_input = input("Please Enter your choice: ")
            else:
                print("Please enter a number and not a string!")
                user_input = input("Please Enter your choice: ")
    return lst

def is_list_equal(lst1, lst2):
    if lst1 == lst2:
        return True
    else:
        return False


def print_for_exact_time(lst):
    print(lst, end='', flush=True)
    time.sleep(0.7)
    print('\r' + ' ' * len(lst), end='', flush=True)
    print()

def play(difficulty):
    gen_lst = generate_sequence(difficulty)
    print_for_exact_time(gen_lst)
    user_lst = get_list_from_user(difficulty)
    result = is_list_equal(gen_lst, user_lst)
    if result:
        print("You won!")
        return True
    else:
        print("You lost!")
        return False

