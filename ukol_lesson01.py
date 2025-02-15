#rozdělení stringu
print("Prvních 5 písmen:")
print("indexování"[:5])
print("Posledních 5 písmen:")
print("indexování"[5:10])
print("Každé 3. písmeno (počínaje prvním) od 'i':")
print("indexování"[::3])

#převaděč jednotek
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26
kg_pocet = 80
km_pocet = 54
l_pocet = 5

vypocet_kg = (kg_lb * kg_pocet)
vypocet_km = (km_mile * km_pocet)
vypocet_l = (l_gal * l_pocet)

print(kg_pocet, "kg je", vypocet_kg, "lb")
print(km_pocet, "km je", vypocet_km, "mil")
print(l_pocet, "l je", vypocet_l, "gal")

#nakupujeme auto
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva_merc = 5000

cena_2_merc = int(mercedes) *2
cena_merc_a_rolls = int(mercedes + rolls_royce)
cena_2_rolls_s_vybavou = int(rolls_royce + vybava) *2
cena_merc_s_vybavou = int(mercedes + vybava)
merc_se_slevou = int(mercedes - sleva_merc)

print("Sleva na Mercedes: ", sleva_merc)
print("Cena za dva Mercedesy je: ", cena_2_merc)
print("Cena za Mercedes a Rolls-Royce: ", cena_merc_a_rolls)
print("Cena za dva Rolls-Royce s příplatkovou výbavou: ", cena_2_rolls_s_vybavou)
print("Cena za Mercedes s příplatkovou výbavou: ", cena_merc_s_vybavou)
print("Cena za Mercedes po slevě: ", merc_se_slevou)

#spojování stringů
jmeno = "Lukáš"
prijmeni = "Dvořák"
znak = "="
delka_jmena = len(jmeno + prijmeni)

print("Celé jméno: ", jmeno + " " + prijmeni)
print("Délka jména: ", delka_jmena + 1)
print(znak * delka_jmena)
print(jmeno + " " + prijmeni)
print(znak * delka_jmena)