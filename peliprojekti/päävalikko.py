# Kysytään pelaajan nimi ja ikä, ja selvitetään onko pelaaja tarpeeksi vanha peliä varten.
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
        print("\nPelin ikäraja on K12, olet liian nuori pelaamaan peliä!\n")
        exit()
    else:
        print(f"\nHei {pelaajan_nimi}, tervetuloa pelaamaan peliä!")

    return pelaajan_nimi, pelaajan_ikä


# Tulostetaan näkyviin toistuva päävalikko. Päävalikossa voi aloittaa pelin, tulostaa pelaajan tiedot, antaa lisätietoja pelaajasta, ja lopettaa ohjelman.
def päävalikko(pelaajan_nimi, pelaajan_ikä):

    tietolista = [pelaajan_nimi, pelaajan_ikä, "", ""]

    while True:

        print("\nPäävalikko\n\nPäävalikossa voit valita erilaisia toimintoja:\n1) Aloita peli\n2) Näytä tietoni\n3) Kerro lempipelisi\n4) Kerro muuta tietoa itsestäsi\n\n'lopeta' -> Lopeta ohjelma")
        pyydetty_toiminto = input("\nKirjoita toiminnon numero ja paina enteriä!\nKutsu toiminto: ")

        if pyydetty_toiminto.lower() == str("lopeta"):
            print("\nPeli sulkeutuu.\n")
            exit()

        try:
            pyydetty_toiminto = int(pyydetty_toiminto)
        except ValueError:
            input("Annoit virheellisen numeron, yritä uudelleen. (Paina enteriä jatkaaksesi)")
            continue

        # if pyydetty_toiminto == 0:
        #     print("\nPeli sulkeutuu.\n")
        #     exit()
        if pyydetty_toiminto == 1:
            return pelaajan_nimi
        elif pyydetty_toiminto == 2:
            tulosta_tiedot(tietolista)
        elif pyydetty_toiminto == 3:
            tietolista[2] = lempi_peli()
        elif pyydetty_toiminto == 4:
            tietolista[3] = muu_tieto()
        else:
            input("Numerolla ei löytynyt toimintoa. (Paina enteriä jatkaaksesi)")
  

def tulosta_tiedot(tietolista):

    print("\n-- Pelaajan tiedot-- ")
    print("   Nimi:", tietolista[0])
    print("   Ikä:", tietolista[1])

    if tietolista[2] != "":
        print("   Lempipelisi:", tietolista[2])
    if tietolista[3] != "":
        print("   Muuta tietoa sinusta:", tietolista[3])

    input("\nPaina enteriä jatkaaksesi")


def lempi_peli():
    lempipeli = input("\nKerro lempipelisi: ")
    return lempipeli

def muu_tieto():
    tieto = input("\nKerro muuta tietoa itsestäsi: ")
    return tieto