# ukol 1
veta = str('Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu')
print(f"Program, který spočítá kolik samohlásek a souhlásek obsahuje \nVěta: {veta}")

samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'

vysledek = dict()
soucet_samohlasek = 0
soucet_souhlasek = 0

for znak in veta.lower():
    if znak in samohlasky:
        soucet_samohlasek +=1

for znak in veta.lower():
    if znak in souhlasky:
        soucet_souhlasek += 1

vysledek["Počet souhlásek:"] = [soucet_samohlasek]
vysledek["Počet samohlásek:"] = [soucet_souhlasek]

print("Počet souhlásek:", vysledek['Počet samohlásek:'][0],"|", "Počet samohlásek:", vysledek['Počet souhlásek:'][0])

# ukol 2
cisla = [1, 2, 3, 4, 5, 6, 7, 8]
liche = 0
sude = 0

for cislo in cisla:
    if cislo % 2 == 0:
        sude += cislo
    else:
        liche += cislo

vysledek = abs(sude - liche)
print("rozdíl", vysledek)

# ukol 3
# Zadaná proměnná
vysledek = []

# Zadané hodnoty: počáteční hodn., konečná hodn., dělitel
start = 3
stop = 9
delitel = 3

if isinstance(start, int) \
        and isinstance(stop, int) \
        and isinstance(delitel, int):
    print("Zadaný rozsah: <", start, ", ", stop, ">", sep="")

    # Iteruj skrze rozsah zadaných čísel
    for number in range(start, stop + 1):
        # .. pokud je vybrané číslo dělitelné hodnotou v prom. "delitel"
        if number % int(delitel) == 0:
            # .. přidej jej do seznamu "vysledek"
            vysledek.append(number)
    # doplň výpis hodnot v proměnné 'vysledek'
    print('Čísla dělitelná', delitel, ':', vysledek)

else:
    print("Zadané vstupy musí být čísla.")

# ukol 4
seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
delky_slov = dict()

for slovo in seznam_slov:
    delky_slov[slovo] = [len(slovo)]

print(delky_slov)
