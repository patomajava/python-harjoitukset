def pelaajan_tiedot():

    print("\nTervetuloa pelaamaan peliä!")

    pelaajan_nimi = input("\nPelaajan nimi: ")

    while True:
        try:
            pelaajan_ikä = int(input("Pelaajan ikä: "))
            break
        except ValueError:
            print("Annettu ikä on virheellinen luku.")


    if pelaajan_ikä < 12:
        print("\nPelin ikäraja on K12, olet liian nuori pelaamaan peliä!")
        exit()
    else:
        print(f"\nHei {pelaajan_nimi}, tervetuloa pelaamaan peliä!")

    return pelaajan_nimi, pelaajan_ikä


def päävalikko():

    print("\nPäävalikko\n\nPäävalikossa voit valita erilaisia toimintoja:\n1) Aloita peli\n2) Näytä tietoni\n3) Kerro lempipelisi\n4) Kerro muuta tietoa itsestäsi\n0) Lopeta ohjelma")

    pyydetty_ohjelma = input("\nKirjoita toiminnon numero ja paina enteriä!\nKutsu toiminto: ")
    return pyydetty_ohjelma

def aloita_peli():
    input("\nPeli on vielä kesken :) (Paina enteriä jatkaaksesi)")
  

def tulosta_tiedot(tietolista):

    print("\nPelaajan tiedot")

    print("Nimi:", tietolista[0])
    print("Ikä:", tietolista[1])

    if tietolista[2] != "":
        print("Lempipelisi:", tietolista[2])
    if tietolista[3] != "":
        print("Muuta tietoa sinusta:", tietolista[3])

    input("\nPaina enteriä jatkaaksesi")


def lempi_peli():
    lempipeli = input("\nKerro lempipelisi: ")
    return lempipeli

def muu_tieto():
    tieto = input("\nKerro muuta tietoa itsestäsi: ")
    return tieto