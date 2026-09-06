print("\nTervetuloa pelaamaan peliä!")
pelaajan_nimi = str(input("\nKirjoita nimesi: "))
pelaajan_ika = int(input("Kirjoita ikäsi: "))
lempipeli = ""
lempiartisti = ""

if pelaajan_ika < 12:
    print(f"\nHei {pelaajan_nimi}! Pelin ikäraja on K12. ")
    exit()

else:
    print(f"\nHei {pelaajan_nimi}, tervetuloa pelaamaan!")

while True:
    print("\nPäävalikko\n")
    print("Voit kutsua erilaisia ohjelmia:\n1) Aloita peli\n2) Tulosta tietoni\n3) Lempipeli\n4) Lempiartisti\n0) Lopeta ohjelma")

    haluttu_ohjelma = input("\nMitä ohjelmaa haluat kutsua? ")

    if haluttu_ohjelma == "":
        input("\nTuota ohjelmaa ei ole olemassa.")
    elif int(haluttu_ohjelma) == 0:
        print("Ohjelma sammuu.")
        exit()
    elif int(haluttu_ohjelma) == 1:
        input("\nPeli on vielä kesken :( ")
    elif int(haluttu_ohjelma) == 2:
        input(f"\nTiedot sinusta:\n\nNimesi: {pelaajan_nimi}\nIkäsi: {pelaajan_ika}\nLempipelisi: {lempipeli}\nLempiartistisi: {lempiartisti}")
    elif int(haluttu_ohjelma) == 3:
        lempipeli = str(input("\nKirjoita lempipelisi: "))
    elif int(haluttu_ohjelma) == 4:
        lempiartisti = str(input("\nKirjoita lempiartistisi: "))
    else:
        input("\nTuota ohjelmaa ei ole olemassa.")