import random
import numpy as np
from constants import WORD_LENGTH, ACCEPTABLE_WORDS_LIST, LIVES, GAME_DISPLAY

def user_input():
    user_choice = input(f'Choose a {WORD_LENGTH} letter word: ').lower()
    if len(user_choice) > WORD_LENGTH:
        print(f"Sorry only {WORD_LENGTH} letter words are allowed\n Try again")
    elif user_choice not in ACCEPTABLE_WORDS_LIST:
        print("Not a valid word\n please try again")
    else:
        return np.array(list(user_choice))

def green_box_check(user_choice, computer_choice, num):
    if np.array_equal(user_choice[num], computer_choice[num]):
        GAME_DISPLAY.append('🟩')
        return 'Green'
    

def yellow_box_check(user_choice, computer_choice, num):
    if user_choice[num] in computer_choice:
        GAME_DISPLAY.append('🟨')
        return 'Yellow'


computer_choice = np.array(list(random.choice(ACCEPTABLE_WORDS_LIST)))

print(computer_choice)

while LIVES > 0:

    user_choice = user_input()

    if type(user_choice) == "NoneType":
        pass
    else:
        for num in range(len(user_choice)):
            if green_box_check(user_choice, computer_choice, num) == 'Green':
                print('Green')
            elif yellow_box_check(user_choice, computer_choice, num) == 'Yellow':
                print('Yellow')
            else:
                GAME_DISPLAY.append('⬛')
                print('Black')
        LIVES -= 1








