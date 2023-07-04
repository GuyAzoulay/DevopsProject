import random



def generate_number(difficulty):
    return random.randint(1, difficulty )


def get_guess_from_user(difficulty):
    choose_correct = False
    user_input = input(f"Please guess a number between 1 to {difficulty}: ")
    while not choose_correct:
        if user_input.isnumeric():
            if int(user_input) < 1 or int(user_input) > difficulty:
                print(f"Please enter a number between 1 - {difficulty}!")
                user_input = input("Please Enter your choice: ")
            else:
                choose_correct = True
                return int(user_input)
        else:
            print("Please enter a number and not a string!")
            user_input = input("Please Enter your choice: ")

    return user_input

def compare_results(difficulty, secret_number):
    if difficulty == secret_number:
        return True
    else:
        return False

def play(difficulty):
    gen_num = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    result = compare_results(gen_num, user_guess)
    if result:
        print("You won!")
        return True
    else:
        print("You lost!")
        return False
