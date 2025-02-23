'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author = Lukáš Bystroň
email: lbystron@gmail.com
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# pomocný list
velka_pismena = 0
zacinaji_velkym_pismem = 0
mala_pismena = 0
cisla = 0
pocet_slov = 0
text = set()
pocet_pis = dict()

# oddělovač
znak = "-" *40

# přihlášení
username = input("username:")
password = input("password:")
print(znak)

# registrováni uživatele
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# přístupu uživatele a výběr textu uživatelem
if uzivatele.get(username) == password:
    print("Welcom to the app,", username,"\n","We have 3 texts to be analyzed.","\n",znak)
    vyber_textu = int(input("Enter a number btw. 1 and 3 to select: "))
    if vyber_textu == 1:
        text = TEXTS[0].split()
        print(znak)
    elif vyber_textu == 2:
        text = TEXTS[1].split()
        print(znak)
    elif vyber_textu == 3:
        text = TEXTS[2].split()
        print(znak)
    else:
        ("You have made a wrong selection. The program ends.")
else: 
    print("Unregistered user, terminating the program..") 

# rozdělení textu podle zadání
for slovo in text:
    if slovo.islower():
        mala_pismena += 1
    elif slovo[0].isalpha():
        zacinaji_velkym_pismem += 1
    elif slovo.isnumeric():
        cisla += 1
    elif slovo.isupper():
        velka_pismena += 1

# soucet cislic v textu
sum = 0
for cislo in TEXTS[0].split():
    if cislo.isnumeric():
        sum += int(cislo)

# počet pismen ve slově
for slovo in text:
    if slovo[0].isalpha():
        pocet_pis[slovo] = [len(slovo) * "*"]

# vysledek
print(f'''There are {len(text)} words in the selected text.
There are {zacinaji_velkym_pismem} titlecase words.
There are {velka_pismena} uppercase words.
There are {mala_pismena} lowercase words.
There are {cisla} numeric strings.
The sum of all the numbers {sum}\n''', znak
)

#počet písmenek
print(f'''LEN|  OCCURENCES  |NR.\n {znak}
  1|hvezda        |cislo
  2|              |cislo
  3|              |cislo
  4|              |cislo
  5|              |cislo
  6|              |cislo
  7|              |cislo
  8|              |cislo
  9|              |cislo
 10|              |cislo
 11|              |cislo'''
)