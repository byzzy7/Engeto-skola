from time import time
import random

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

def user_choice(aa, cc, dd, gg):
    pokracovani = True
    while pokracovani:
        try:
            aa = int(input(">>> "))
            if aa != dd:
                cc += 1
                print(f"{gg}\n{znak}")
            else:
                print(f"Correct, you've guessed the right number\nin {cc} guesses!\n{znak}\nThat´s amazing!")
                pokracovani = False
        except ValueError:
            print("Numbers only")

def bull(uz):
        uz.count(uz)

start = time() # stopky - zacatek
znak = "-" * 47  # oddělovací čárka
cisla_uzivatel = [] # seznam čísel od uživatele
cisla_random = [] # seznam čísel od PC nahodne
guesses = 0 #pocet pokusu
pocet_cisel = []

#uvitání hráče a představení hry
print(f'''Hi there!\n{znak} 
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.\n{znak}\nEnter a number:\n{znak}'''
)

#vylosované číslo pro hádnání
PC_nahodne = random_number()
print("TEST tipované číslo:", PC_nahodne)
uzivatel = int(input(">>> "))
print(pocet_cisel,"\n", znak)

#rozdělení čísla do seznamu od uživatele a nahodné
rozdil_seznamu = [value for value in cisla_uzivatel if value in cisla_random] # vyhledani stejnych cisel uzivate vs PC
bull(uz=cisla_uzivatel)
set_of_numbers(cislo_od_uzivatele=uzivatel, cisla_od_PC=PC_nahodne)
user_choice(aa=uzivatel, cc=guesses, dd=PC_nahodne, gg=pocet_cisel)
end = time() # stopky - konec
x = round(end - start,2) #výsledek jak dlouho hádal uživatel

print("TEST uzivatel", uzivatel)
print("TEST bull", bull)
print("TEST vypisu", cisla_uzivatel)
print("TEST vypisu", cisla_random)
print("TEST vypis rozdilu", rozdil_seznamu)

#vypis statistiky
print(f"{znak}\nStatistika:",statistics(PC_nahodne, guesses, x))