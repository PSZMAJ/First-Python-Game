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
    name = str(input('Graczu podaj swoje imie: '))
    # sprawdzenie imienia
    while name.isalpha() != True:
         name = input('Graczu, podałeś niepoprawne imie, podaj swoje imie: ')
   
    print('Twoje imie to {}'.format(name))
    time.sleep(2)
    print('Trwa generowanie liczb...')
    time.sleep(2)
    tajna_liczba = (random.randint(1,31))
 
    # logika gry
    
    
    for runda in range(2):
        liczba = int(input('Podaj liczbę z zakresu 1,3'))
        if liczba == tajna_liczba:
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
    print('test')
    
language = int(input('PLEASE SELECT LANGUAGE: '))

if language == 1:
    PL_GAME()
else:
    ENG_GAME()


