import pygame
import random
import time
import ptext
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("GoType")

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
purple = (255,0,255)
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
orange = (255,128,0)
aqua = (0,204,204)
pink = (175,0,175)
grey = (127.5, 127.5, 127.5)

colors = [blue, red, green, purple, white, yellow, orange, aqua, pink]
width = random.randint(50,100)
height = random.randint(50,100)

def randcolor():
    randomcolor = (random.randint(10,245), random.randint(10,245), random.randint(10,245))
    return randomcolor

def string_chunks(string, x):
    lstring = string.split()
    new_list = []
    counter = 0
    for word in lstring:
        if counter%x == 0 and counter!= 0:
            word += "\n"
        counter += 1
        new_list.append(word)
    new = " ".join(new_list)
    return new

#comic sans text
def show_text_cs(msg, pos, color):
    x, y = pos
    if 20*(len(msg)) + x > screen.get_width():
        average = 5
        char_per_line = (screen.get_width())/(17)
        char_per_line = int(char_per_line)
        word_per_line = int(char_per_line/average)
        text = string_chunks(msg, word_per_line - 2)
        ptext.draw(text, pos, sysfontname="comicsansms", color= color, fontsize = 25)
    else:
        ptext.draw(msg, pos, sysfontname="comicsansms", color= color, fontsize = 25)

def show_text_arial(msg, x, y, color):
    fontobj = pygame.font.SysFont("arial", 60)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj,(x,y))

def button(msg, dimensions, position, color, text_color):
    width, height = dimensions
    x, y = position
    pygame.draw.rect(screen,color,[x,y,width,height])
    fontobj = pygame.font.SysFont("arial", 15)
    msgobj = fontobj.render(msg, False, text_color)
    screen.blit(msgobj,(x+5,y+5))


word = ""

sentences_medium = {"Sometimes there isn't a good answer. No matter how you try to rationalize the outcome, it doesn't make sense. And instead of an answer, you are simply left with a question. Why?" : 32,\
    "Betty was a creature of habit and she thought she liked it that way. That was until Dave showed up in her life. She now had a choice to make and it would determine whether her life remained the same or if it would change forever.": 46,\
    "She glanced up into the sky to watch the clouds taking shape. First, she saw a dog. Next, it was an elephant. Finally, she saw a giant umbrella and at that moment the rain began to pour.":37}

sentences_hard = {"The introduction can be anywhere from a paragraph to a page, depending on the requirements and circumstances. Use this opportunity to introduce the main idea, provide any pertinent definitions, and briefly describe what will be covered. Above all else, the introduction must clearly state what readers are about to explore. Be sure to steer clear of any evidence of your opinion on the topic." : 64,\
    "It was the best compliment that he'd ever received although the person who gave it likely never knew. It had been an off-hand observation on his ability to hold a conversation and actually add pertinent information to it on practically any topic. Although he hadn't consciously strived to be able to do so, he'd started to voraciously read the news when he couldn't keep up on topics his friends discussed because their conversations went above his head.": 77, \
    "Her hair was a tangled mess which she tried to make presentable by putting in a lump on the top of her head. It didn't really work although it was a valiant attempt. While most people simply noticed the tangled mess on top of her head, what most people failed to understand that within the tangles mess was an entirely new year. That was her secret. She kept worlds on top of her head.": 74,\
    "Betty was a creature of habit and she thought she liked it that way. That was until Dave showed up in her life. She now had a choice to make and it would determine whether her life remained the same or if it would change forever.": 46}

sentence_keys = list(sentences_hard.keys())

sentence_values = list(sentences_hard.values())

len_keys = len(sentence_keys)

text_color = green

m = random.randint(0, len_keys-1)

sentence = sentence_keys[m]

wpm = 0

#game loop
while True:

    length = len(word)

    if length == 1:
        start_time = time.time()

    #clear screen
    screen.fill(black)
   
    #draw all items
    show_text_cs(sentence, (30, 100), grey)

    show_text_cs(sentence[:length], (30, 100), black)

    show_text_cs(word + "|", (30, 100), text_color)

    if wpm != 0:
        screen.fill(black)
        show_text_arial(str(wpm) + " words per minute", 200, 100, yellow)
        button("Play Again", (125, 40), (200,300) , aqua, yellow)
        button("Quit", (125,40), (500,300) , pink, yellow)
        answer = ""
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 200 <= mouse_x and mouse_x <= 325 and 300 <= mouse_y and mouse_y <= 340:
                    answer = "continue"
                elif 500 <= mouse_x and mouse_x <= 625 and 300 <= mouse_y and mouse_y <= 340:
                    answer = "quit"
        if answer == "continue":
            new = random.randint(0, len_keys-1)
            sentence = sentence_keys[new]
            wpm = 0
            word = ""
        elif answer == "quit":
            break


    #check for events and change statuses/variables
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            #shift 0-9
            if event.key == pygame.K_1 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "!"
            elif event.key == pygame.K_2 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "@"
            elif event.key == pygame.K_3 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "#"
            elif event.key == pygame.K_4 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "$"
            elif event.key == pygame.K_5 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "%"
            elif event.key == pygame.K_6 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "^"
            elif event.key == pygame.K_7 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "&"
            elif event.key == pygame.K_8 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "*"
            elif event.key == pygame.K_9 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "("
            elif event.key == pygame.K_0 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += ")"
            #rest of the special symbols
            elif event.key == pygame.K_COMMA and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "<"
            elif event.key == pygame.K_PERIOD and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += ">"
            elif event.key == pygame.K_SLASH and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "?"
            elif event.key == pygame.K_SEMICOLON and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += ":"
            elif event.key == pygame.K_QUOTEDBL and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += '"'
            ##uppercase
            elif (event.key >= 97 and event.key <= 123) and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                letter = chr(event.key - 32)
                word += letter
            #lowercase
            elif (event.key >= 48 and event.key <=56) or (event.key >= 97 and event.key <= 123):
                letter = chr(event.key)
                word += letter
            #more special symbols
            elif event.key == 8:
                word = word[:-1]
            elif event.key == pygame.K_SPACE:
                word += " "
            elif event.key == pygame.K_PERIOD:
                word += "."
            elif event.key == pygame.K_COMMA:
                word += ","
            elif event.key == pygame.K_SLASH:
                word += "/"
            elif event.key == pygame.K_BACKSLASH:
                word += "\\"
            elif event.key == pygame.K_SEMICOLON:
                word += ";"
            elif event.key == pygame.K_RETURN:
                word += "\n"
            elif event.key == pygame.K_QUOTE:
                word += "'"
            elif event.key == 45:
                word += "-"

            length = len(word)

            if (word) == (sentence):
                end_time = time.time()
                total_time = end_time - start_time
                total_time = int(round(total_time))
                min_total_time = (total_time)/60
                wpm = (sentence_values[m])/(min_total_time)
                wpm = int(round(wpm))
            elif word == sentence[:length]:
                text_color = green
                continue
            else:
                text_color = red

            #insert "do you want to place again" stuff here

    #update
    pygame.display.update()