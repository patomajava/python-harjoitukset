pelaajan_nimi = str(input("\nKirjoita nimesi: "))
pelaajan_ika = int(input("Kirjoita ikäsi: "))

if pelaajan_ika < 12:
    print(f"\nHei {pelaajan_nimi}! Pelin ikäraja on K12. ")
    exit()

else:
    print(f"\nHei {pelaajan_nimi}, tervetuloa pelaamaan!")

while 0 == 0:
    print("\nPäävalikko\n")
    print("Tässä valikossa voit kutsua erilaisia ohjelmia:\n1) Lempipeli\n2) Lempiartisti\n0) Lopeta ohjelma")

    haluttu_ohjelma = int(input("\nMitä ohjelmaa haluat kutsua: "))

    if haluttu_ohjelma == 0:
        print("Ohjelma sammuu.")
        exit()
    elif haluttu_ohjelma == 1:
        lempipeli = str(input("\nMikä on lempipelisi? "))
    elif haluttu_ohjelma == 2:
        lempiartisti = str(input("\nKuka on lempiartistisi? "))
    else:
        print("Tuolla numerolla ei löytynyt ohjelmaa.")