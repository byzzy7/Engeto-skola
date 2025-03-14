from time import strftime
import random

znak = "-" * 47  # oddělovací čárka

#uvitání hráče a představení hry
print(f'''Hi there!\n{znak} 
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.\n{znak}'''
)

def time_now():
    '''aktualní čas'''
    return strftime("%X")

def random_number():
    ''' vygenerování náhodného čtyřmístného čísla
    a nesmí začínat 0
    '''
    return random.randint(1000, 9999)

def evaluation(uzivatel, hadane, pokus):
    '''
    Vyhodnoceni vstupu, jestli uzivatel
    uhadl nějaké číslo
    '''
    pokus += 1
    if uzivatel == hadane:
        return "čislo udohnute"
    else:
        return "nenene"

def statistics(hadane_cislo, pocet_hadani, cas):
    '''
    Shromaždění údajů pro Statistiky
    Počet hádaní, Hádané číslo, Čas
    '''
    return {
        "Hadane_cislo": hadane_cislo,
        "Počet_hadani": pocet_hadani,
        "Čas": cas
    }

#pocet pokusu
guesses = 0
#vylosované číslo pro hádnání
evaluation.guessed_number = random_number()

#Vypis hadaneho cisla
print("Tipované číslo:", evaluation.guessed_number)
#vstup uživatele a vygenoravni nahodneho cisla
print(evaluation(int(input("Zadej číslo: ")),evaluation.guessed_number, guesses))
#vypis statistiky
print("Statistika:",statistics(evaluation.guessed_number, guesses, time_now()))