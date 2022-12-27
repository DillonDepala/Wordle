import random as rand
import numpy as np
from constants import WORD_LENGTH, ACCEPTABLE_WORDS_LIST, LIVES, GAME_DISPLAY, RUNNING

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

def game_won_check(game_display):
    if game_display == ['🟩', '🟩', '🟩', '🟩', '🟩']:
        print('Congratulations you win!')
        return True

def game_lost_check(lives, game_display, comp_choice):
    if lives == 0 and game_display != ['🟩', '🟩', '🟩', '🟩', '🟩']:
        print('YOU LOSE')
        print(f'The word is: {comp_choice}')
        return True



computer_choice = np.array(list(rand.choice(ACCEPTABLE_WORDS_LIST)))

print(computer_choice)

while LIVES > 0 and RUNNING:

    user_choice = user_input()
    LIVES -= 1

    if isinstance(user_choice, type(None)) is True:
        pass
    else:
        for num in range(len(user_choice)):
            if green_box_check(user_choice, computer_choice, num) == 'Green':
                pass
            elif yellow_box_check(user_choice, computer_choice, num) == 'Yellow':
                pass
            else:
                GAME_DISPLAY.append('⬛')

        print(GAME_DISPLAY)
        if game_won_check(GAME_DISPLAY) == True:
            RUNNING = False
        
        if game_lost_check(LIVES, GAME_DISPLAY, computer_choice) ==True:
            RUNNING = False

        GAME_DISPLAY = []