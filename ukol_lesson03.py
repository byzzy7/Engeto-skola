sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
oddelovac = "=" * 62
film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}
film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}
film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}

# kompletní seznam
filmy = dict()

filmy[film_1["jmeno"]] = film_1
filmy[film_2["jmeno"]] = film_2
filmy[film_3["jmeno"]] = film_3

print("\tVÍTEJ V NAŠEM FILMOVÉM SLOVNÍKU!" + "\n" + oddelovac)
print(sluzby[0], "|", sluzby[1], "|", sluzby[2], "\n" + oddelovac)
print("Dostupne filmy:" + "\n" + oddelovac + "\n" + filmy[film_1["jmeno"]]["jmeno"] + ", " + filmy[film_2["jmeno"]]["jmeno"] + ", " + filmy[film_3["jmeno"]]["jmeno"] + "\n" + oddelovac)

# detail filmu
detail_filmu = input("Detail_filmu: ")
if detail_filmu == film_1["jmeno"]:
    print(filmy[film_1["jmeno"]], "\n", oddelovac)
elif detail_filmu == film_2["jmeno"]:
    print(filmy[film_2["jmeno"]], "\n", oddelovac)
elif detail_filmu == film_3["jmeno"]:
    print(filmy[film_3["jmeno"]], "\n", oddelovac)
else:
    print("Špatný název")

print("Všichní režiséři:" + "\n" + oddelovac)
print(filmy[film_1["jmeno"]]["reziser"],", ", filmy[film_2["jmeno"]]["reziser"],", ", filmy[film_3["jmeno"]]["reziser"])