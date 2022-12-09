import random 
import pygame

#----------------------------------------------------------UI DESIGN-----------------------------#
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Wordle :)")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()








#----------------------------------------------------------GAME DESIGN---------------------------#
WORD_LIST = ['hello', 'merry']
DISPLAY = []
GAME_DISPLAY = []
REF = 0
ATTEMPTS = 6
COMPLETE = False

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
   

computer_choice_list =[]
player_choice_list = []


computer_choice = random.choice(WORD_LIST).upper()
for x in computer_choice:
    computer_choice_list.append(x)

print(computer_choice)

while ATTEMPTS > 0 and COMPLETE == False:
    player_choice = input('CHOOSE WORD ').upper()
    for y in player_choice:
        player_choice_list.append(y)
       
    for x in player_choice_list:
        box_check(x)
        REF+=1
    
    ATTEMPTS -= 1

    print(DISPLAY)
    print(GAME_DISPLAY)
    
    REF = 0
    player_choice_list = []
    DISPLAY =[]
    if GAME_DISPLAY == ['🟩', '🟩', '🟩', '🟩', '🟩']:
        COMPLETE = True
    GAME_DISPLAY=[]
    

    



