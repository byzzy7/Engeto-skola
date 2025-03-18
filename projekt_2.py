from time import strftime, time
import random

def time_now():
    '''aktualní čas'''
    return strftime("%X")

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

def memory():
    dd.append(uzivatel_cislo)

def user_choice():
    pass

def evaluation(rozdil):
    if rozdil != None:
        print(f"{rozdil} cows\n{znak}")
    else:
        print(f"0 cows\n{znak}")

start = time() # začátek počítání času
znak = "-" * 47  # oddělovací čárka
cisla_uzivatel = [] # seznam čísel od uživatele
cisla_random = [] # seznam čísel od PC nahodne
guesses = 0 #pocet pokusu
dd = [] # ulozeni vsech tipovanych cisel

#uvitání hráče a představení hry
print(f'''Hi there!\n{znak} 
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.\n{znak}'''
)

#vylosované číslo pro hádnání
PC_nahodne = random_number()
#uzivatel_cislo = int(input("Enter a number: "))

print("TEST Tipované číslo:", PC_nahodne)

pokracovat = True
while pokracovat:
    uzivatel_cislo = int(input("Enter a number: "))
    memory()
    set_of_numbers(uzivatel_cislo, PC_nahodne)
    if uzivatel_cislo == PC_nahodne:
        pokracovat = False
        print(f"{znak}\n>>> {uzivatel_cislo}\nUhadl jsi!")
    else:
        guesses += 1
        print("Znovu")


#rozdělení čísla do seznamu od uživatele a nahodné
#set_of_numbers(uzivatel_cislo, PC_nahodne)
rozdil_seznamu = [value for value in cisla_uzivatel if value in cisla_random] # vyhledani stejnych cisel uzivate vs PC
evaluation(rozdil_seznamu)
end = time() #začátek počítání času
x = round(end - start,2) #výsledek jak dlouho hádal uživatel


print("TEST vypisu", cisla_uzivatel)
print("TEST vypisu", cisla_random)
print("TEST vypis rozdilu", rozdil_seznamu)

#vypis statistiky
print(f"{znak}\nStatistika:",statistics(PC_nahodne, guesses, x))