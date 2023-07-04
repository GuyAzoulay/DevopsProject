from Utils import *

def add_score(difficulty):

    POINTS_OF_WINNING = (difficulty * 3) + 5
    with open (SCORE_FILE_NAME, "w") as score_file:
        score_file.write(str(POINTS_OF_WINNING))
    return POINTS_OF_WINNING
