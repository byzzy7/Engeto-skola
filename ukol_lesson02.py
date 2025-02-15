heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
heslo_3 = "123456"      # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"

#podmínky
heslo = heslo_6
zadani_hesla = input("Zadejte heslo: ")
pocet_pozic = len(zadani_hesla)
min_delka_hesla = 8
znak = ["@", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#kontrola vypisu
#print(f"KONTROLA: prvni_pozice_hesla: {zadani_hesla[0]}, pocet: {pocet_pozic}, znak '@': {"@" in zadani_hesla}")

#funkce
if zadani_hesla == heslo:
    print("Heslo je v pořádku")
elif zadani_hesla == heslo_0:
    print("Vynechal jsi pole s heslem!")
elif zadani_hesla[0] in znak[1:11]:
    print("Heslo nesmí začínat číselným znakem")
elif zadani_hesla.isnumeric():
    print("Heslo nesmí začínat číselným znakem")
elif zadani_hesla.isalpha():
    print("Heslo musí obsahovat jak číselné znaky, tak písmena")
elif znak[0] in zadani_hesla:
    print("Heslo nesmí obsahovat '@'")
elif pocet_pozic < min_delka_hesla:
    print("Heslo musí být alespoň 8 znaků dlouhé")
else:
    print("Špatné heslo")
