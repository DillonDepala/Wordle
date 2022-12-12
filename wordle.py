import random
import re
from collections import Counter
from operator import itemgetter

import requests

# import pygame

# #----------------------------------------------------------UI DESIGN-----------------------------#
# pygame.init()

# win = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("Wordle :)")

# x = 50
# y = 50
# width = 40
# height = 60
# vel = 5

# run = True

# while run:
#     pygame.time.delay(100)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
    
#     pygame.display.update()

# pygame.quit()








#----------------------------------------------------------GAME DESIGN---------------------------#
DISPLAY = []
GAME_DISPLAY = []
REF = 0
ATTEMPTS = 6
COMPLETE = False
IRRELEVANT_LETTERS_LIST = []

def box_check(letter):
    if letter == computer_choice_list[REF]:
        DISPLAY.append(letter)
        GAME_DISPLAY.append('🟩')
    elif letter in computer_choice_list:
        DISPLAY.append(letter)
        GAME_DISPLAY.append('🟨')
    elif letter not in computer_choice_list:
        DISPLAY.append('_')
        GAME_DISPLAY.append('⬛')
        if letter not in IRRELEVANT_LETTERS_LIST:
            IRRELEVANT_LETTERS_LIST.append(letter)
   

computer_choice_list =[]
player_choice_list = []

meaningpedia_resp = requests.get(
    "https://meaningpedia.com/5-letter-words?show=all")

# get list of words by grabbing regex captures of response
# there's probably a far better way to do this by actually parsing the HTML
# response, but I don't know how to do that, and this gets the job done

# compile regex
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
# find all matches
five_letter_word_list = pattern.findall(meaningpedia_resp.text)


computer_choice = random.choice(five_letter_word_list).upper()
for x in computer_choice:
    computer_choice_list.append(x)

# print(computer_choice)

while ATTEMPTS > 0 and COMPLETE == False:
    print(f'You have {ATTEMPTS} attempts remaining')
    player_choice = input('CHOOSE WORD ').upper()
    for y in player_choice:
        player_choice_list.append(y)
       
    for x in player_choice_list:
        box_check(x)
        REF+=1
    
    ATTEMPTS -= 1

    print(DISPLAY)
    print(GAME_DISPLAY)
    print(f'\nLetters not in word: {IRRELEVANT_LETTERS_LIST}')
    
    REF = 0
    player_choice_list = []
    DISPLAY =[]
    if GAME_DISPLAY == ['🟩', '🟩', '🟩', '🟩', '🟩']:
        print('Congratulations you win!')
        COMPLETE = True

    if ATTEMPTS == 0 and GAME_DISPLAY != ['🟩', '🟩', '🟩', '🟩', '🟩']:
        print('YOU LOSE')
        print(f'The word is: {computer_choice}')
    GAME_DISPLAY=[]
    

IRRELEVANT_LETTERS_LIST = []
    



