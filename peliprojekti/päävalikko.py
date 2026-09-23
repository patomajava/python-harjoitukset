# FUNKTIO, Joka ajetaan kerran ohjelman alussa. Se kysyy pelaajan nimen ja iän sekä määrittää onko pelaaja liian nuori peliä varten.
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


# FUNKTIO, Joka toistaa päävalikkoa jatkuvasti kunnes ohjelma lopetetaan tai peli aloitetaan. Päävalikossa voi pyytää ohjelmaa näyttämään pelaajaan tiedot. Siinä voi myös lisätä tietoja ohjelmalle, tosin ohjelma ei käytä tietoa mihinkään.
def päävalikko(pelaajan_nimi, pelaajan_ikä):

    tietolista = [pelaajan_nimi, pelaajan_ikä, "", ""]

    while True:

        print("\nPäävalikko\n\nPäävalikossa voit valita erilaisia toimintoja:\n[1] Aloita Peli\n[2] Näytä Tietoni\n[3] Kerro Lempipelisi\n[4] Kerro muuta tietoa itsestäsi\n\n[lopeta] -> Lopeta Ohjelma")
        pyydetty_toiminto = input("\nKirjoita toiminnon numero ja paina enteriä!\nKutsu toiminto: ")

        if pyydetty_toiminto.lower() == str("lopeta"):
            print("\nPeli sulkeutuu.\n")
            exit()

        try:
            pyydetty_toiminto = int(pyydetty_toiminto)

        except ValueError:
            input("Annoit virheellisen numeron, yritä uudelleen. (Paina enteriä jatkaaksesi)")
            continue

        if pyydetty_toiminto == 1:
            return "Aloita Peli"
        
        elif pyydetty_toiminto == 2:
            tulosta_tiedot(tietolista)

        elif pyydetty_toiminto == 3:
            tietolista[2] = lempi_peli()

        elif pyydetty_toiminto == 4:
            tietolista[3] = muu_tieto()

        else:
            input("Numerolla ei löytynyt toimintoa.\nPaina [Enter] jatkaaksesi.")
  

# FUNKTIO, Joka tulostaa pelaajan tiedot järjestyksessä, ja sen perusteella mitä tietoa pelaaja on antanut viimeiseksi.
def tulosta_tiedot(tietolista):

    print("\n-- Pelaajan tiedot-- ")
    print("   Nimi:", tietolista[0])
    print("   Ikä:", tietolista[1])

    if tietolista[2] != "":
        print("   Lempipelisi:", tietolista[2])   

    if tietolista[3] != "":
        print("   Muuta tietoa sinusta:", tietolista[3])

    input("\nPaina [Enter] jatkaaksesi.")


def lempi_peli():
    lempipeli = input("\nKerro lempipelisi: ")
    return lempipeli

def muu_tieto():
    tieto = input("\nKerro muuta tietoa itsestäsi: ")
    return tieto