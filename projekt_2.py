from time import time
import random
from collections import Counter

def random_number():
    ''' vygenerování náhodného čtyřmístného čísla
    a nesmí začínat 0
    '''
    return random.randint(1000, 9999)

def set_of_numbers(cislo_od_uzivatele, cisla_od_PC):
    '''
    převední čísla do seznamu
    od uzivatele a PC
    vstup = 1234
    výstup = 1,2,3,4
    '''
    while cislo_od_uzivatele > 0:
        cisla_uzivatel.append(cislo_od_uzivatele % 10)
        cislo_od_uzivatele = cislo_od_uzivatele // 10
    while cisla_od_PC > 0:
         cisla_random.append(cisla_od_PC % 10)
         cisla_od_PC = cisla_od_PC // 10

def statistics(hadane_cislo, pocet_hadani, cas):
    '''
    Shromaždění údajů pro Statistiky
    Počet hádaní, Hádané číslo, Čas
    '''
    return {
        "Hadane cislo": hadane_cislo,
        "Počet hadani": pocet_hadani,
        "Čas": cas
    }

def user_choice(uzivatel, gg):
    while gg != uzivatel:
        uzivatel = int(input(">>> "))
        print("ne","\n", znak)
    print(f"Correct, you've guessed the right number\nin guesses!\n{znak}\nThat´s amazing!")

def bull():
        pass

start = time() # stopky - zacatek
znak = "-" * 47  # oddělovací čárka
cisla_uzivatel = [] # seznam čísel od uživatele
cisla_random = [] # seznam čísel od PC nahodne
guesses = 0 #pocet pokusu

#uvitání hráče a představení hry
print(f'''Hi there!\n{znak} 
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.\n{znak}\nEnter a number:\n{znak}'''
)

#vylosované číslo pro hádnání
PC_nahodne = random_number()
print("TEST tipované číslo:", PC_nahodne)

uzi = int(input(">>> "))
print(znak)
user_choice(uzi, PC_nahodne)
#print(f"Correct, you've guessed the right number\nin {cc} guesses!\n{znak}\nThat´s amazing!")

#rozdělení čísla do seznamu od uživatele a nahodné
rozdil_seznamu = [value for value in cisla_uzivatel if value in cisla_random] # vyhledani stejnych cisel uzivate vs PC
set_of_numbers(cislo_od_uzivatele=uzi, cisla_od_PC=PC_nahodne)
end = time() # stopky - konec
x = round(end - start,2) #výsledek jak dlouho hádal uživatel

print("TEST uzivatel", uzi)
print("TEST vypisu", cisla_uzivatel)
print("TEST vypisu", cisla_random)
print("TEST vypis rozdilu", rozdil_seznamu)

#vypis statistiky
print(f"{znak}\nStatistika:",statistics(PC_nahodne, guesses, x))