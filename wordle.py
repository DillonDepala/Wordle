import random
import numpy as np
from constants import WORD_LENGTH, ACCEPTABLE_WORDS_LIST
import requests

# BLANK_ARRAY = np.array()

def user_input():
    user_choice = input(f'Choose a {WORD_LENGTH} letter word: ').lower()
    if len(user_choice) > WORD_LENGTH:
        raise Exception(f"Sorry only {WORD_LENGTH} letter words are allowed\n Try again")
    elif user_choice not in ACCEPTABLE_WORDS_LIST:
        raise Exception("Not a valid word\n please try again")
    else:
        return user_choice


user_input()








