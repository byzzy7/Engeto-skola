from time import time
import random

def random_number():
    ''' vygenerování náhodného čtyřmístného čísla
    a nesmí začínat 0
    '''
    return random.randint(1000, 9999)

def numbers_from_pc(cisla_od_PC):
    '''
    převední čísla do seznamu
    od PC
    vstup = 1234
    výstup = 1,2,3,4
    '''
    cisla_1 = list()
    while cisla_od_PC > 0:
         cisla_1.append(cisla_od_PC % 10)
         cisla_od_PC = cisla_od_PC // 10
    return numbers_from_pc

def numbers_from_user(cisla_od_uzivatele):
    '''
    převední čísla do seznamu
    od uzivatele
    vstup = 1234
    výstup = 1,2,3,4
    '''
    cisla_2 = list()
    while cisla_od_uzivatele > 0:
         cisla_2.append(cisla_od_uzivatele % 10)
         cisla_od_uzivatele = cisla_od_uzivatele // 10
    return numbers_from_user

def welcome_user(ggg):
    '''uvitání hráče a představení hry'''
    print(f'''Hi there!\n{ggg}\nI've generated a random 4 digit number for you.
    Let's play a bulls and cows game.\n{ggg}\nEnter a number:\n{ggg}'''
    )

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

def bull(uzivatel):
    pass

def cows(ff, hh):
    '''vyhledani stejnych cisel uzivate vs PC'''
    rozdil_seznamu = [value for value in ff if value in hh]
    return rozdil_seznamu

def program_body(PC_nahodne, uzivatel, gg):
    '''
    :param PC_nahodne: vygenerovane nahodne cisla
    :param uzivatel: vlozene nahodne cisla od uzivatele
    :param gg: odelovaci znak radku
    '''
    guesses = 0
    while PC_nahodne != uzivatel:
        guesses += 1
        uzivatel = int(input(">>> "))
        print(f"{cows}\n{gg}")
        print(nahodne)
    print(f"Correct, you've guessed the right number\nin {guesses} guesses!\n{gg}\nThat´s amazing!")
    exit()

start = time() # stopky - zacatek
nahodne = random_number()
znak = "-" * 47
welcome_user(ggg=znak)
program_body(PC_nahodne=nahodne, uzivatel=numbers_from_user, gg=znak)
end = time() # stopky - konec
x = round(end - start,2) #výsledek jak dlouho hádal uživatel
statistics(hadane_cislo=nahodne, pocet_hadani=nahodne,cas=x)