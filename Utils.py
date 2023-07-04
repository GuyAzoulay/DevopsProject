import os
SCORE_FILE_NAME = "Scores.txt"

BAD_RETURN_CODE = -1

def screen_cleaner():
    if not os.path.exists(SCORE_FILE_NAME):
        with open(SCORE_FILE_NAME, 'w') as file:
            file.write("")
    else:
        #if it exist erase it content
        with open(SCORE_FILE_NAME, 'r+') as file:
            file.truncate(0)


    os.system('cls' if os.name == 'nt' else 'clear')