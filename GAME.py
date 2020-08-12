#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 01:23:22 2020

@author: czeburaszka
"""

import time
import random
from selenium import webdriver 


print('LOADING GAME')
time.sleep(2)
print('1-PL')
time.sleep(2)
print('2-ENG')

def PL_GAME():
    time.sleep(2)
    print("""
          
OPIS GRY:
GRA POLEGA NA ZGADNIĘCIU LICZBY Z PEWNEGO ZAKRESU.
JEŚLI ZGADNIESZ LICZBĘ, TO WYGRYWASZ I MOŻESZ PRACOWAĆ NA SWOIM KOMPUTERZE DALEJ.
JEŚLI PRZEGRASZ, SYSTEM AUTOMATYCZNIE POPROSI CIĘ O SUBSKRYBCJĘ KANAŁU AUTORA NA YOUTUBE.
          """)  
          
    time.sleep(4)
    print('Ładuję grę...')
    time.sleep(2)
    name = input('Graczu podaj swoje imie: ')
    # sprawdzenie imienia
    while str(name).isalpha() != True:
         name = input('Graczu, podałeś niepoprawne imie, podaj swoje imie: ')
    
    print('Twoje imie to {}'.format(name))
    time.sleep(2)
    print('Trwa generowanie liczb...')
    time.sleep(2)
    tajna_liczba = (random.randint(1,3))
 
    # logika gry
    
    
    for runda in range(2):
        liczba = input('Podaj liczbę z zakresu 1,3')
        if liczba.isdigit():
            print('')
        else:
            print('nie podales liczby')
        if int(liczba) == tajna_liczba:
            print('Brawo, trafiłeś')
            break
        else:
            runda = runda + 1
            print('Podałeś błędną liczbę.')
            if runda == 2:
                print('Przegrałeś, wylosowana liczba to {}.'.format(tajna_liczba))
                time.sleep(3)
                # ===> uruchomienie okna przeglądarki i szukanie tesktu 'SUBSKRYBUJ' a następnie kliknięcie.
                browser = webdriver.Firefox()
                browser.get('https://www.youtube.com/channel/UC0WP5P-ufpRfjbNrmOWwLBQ')
                linkElm = browser.find_element_by_link_text('SUBSKRYBUJ')
                type(linkElm)
                linkElm.click()
    

    
def ENG_GAME():
    time.sleep(2)
    print("""
          
GAME DESCRIPTION:
GUESSING NUMBER GAME
If You win, You can work in your computer.
If You lose my game will open a browser and i get your subscribe on my YouTube channel.
          """)  
          
    time.sleep(4)
    print('Loading...')
    time.sleep(2)
    name = input('Your name: ')
    # name chceck 
    while str(name).isalpha() != True:
         name = input('Sorry! Your name is incorrect! Please try again : ')
    
    print('Your name is:  {}'.format(name))
    time.sleep(2)
    print('Generating numbers...')
    time.sleep(2)
    secretNumber = (random.randint(1,3))
 
    # logika gry
    
    
    for runda in range(2):
        number = input('Please enter a numer in the range 1,3')
        if number.isdigit():
            print('')
        else:
            print('is not a digit')
        if int(number) == secretNumber:
            print('You Win')
            break
        else:
            runda = runda + 1
            print('Your number is incorrect.')
            if runda == 2:
                print('You lose... , the number is  {}.'.format(secretNumber))
                time.sleep(3)
                # ===> uruchomienie okna przeglądarki i szukanie tesktu 'SUBSKRYBUJ' a następnie kliknięcie.
                browser = webdriver.Firefox()
                browser.get('https://www.youtube.com/channel/UC0WP5P-ufpRfjbNrmOWwLBQ')
                linkElm = browser.find_element_by_link_text('SUBSKRYBUJ')
                type(linkElm)
                linkElm.click()
    
language = int(input('PLEASE SELECT LANGUAGE: '))

if language == 1:
    PL_GAME()
else:
    ENG_GAME()


