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


vyber_textu = len(TEXTS[0])
print(vyber_textu)
znak = "-" *40

# přihlášení
username = str(input("username:"))
password = str(input("password:"))
uzivatele = {"bob": "123"}
print(znak)

# registrováni uživatele
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# vyhodnoceni přístupu
if uzivatele.get(username) == password:
    print("Welcom to the app, ", username, "\n", "We have 3 texts to be analyzed.", "\n", znak)
    vyber_textu = input("Enter a number btw. 1 and 3 to select: ")
    if vyber_textu == 1:
        print("bbb")
    elif vyber_textu == 2:
        print("kjh")
    elif vyber_textu == 3:
        print("kjhg")
    else:
        ("Zdal jste špatný výběr. Program končí")
else:
    print("unregistered user, terminating the program..") 
  


