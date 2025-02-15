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