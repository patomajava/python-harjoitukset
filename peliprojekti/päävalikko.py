import time

def pelaajan_tiedot():

    pelaajan_nimi = input("Pelaajan nimi: ")

    while True:
        try:
            pelaajan_ikä = int(input("Pelaajan ikä: "))
            break
        except ValueError:
            print("Annettu ikä on virheellinen luku.")

    if pelaajan_ikä < 12:
        print("\nPelin ikäraja on K12, olet liian nuori pelaamaan peliä!\n")
        print("Peli sulkeutuu...")
        time.sleep(1.5)
        exit()
    else:
        print(f"\nHei {pelaajan_nimi}, tervetuloa pelaamaan peliä!")
        time.sleep(1.5)

    return pelaajan_nimi, pelaajan_ikä

def päävalikko(tietolista):

    while True:
        print("\033[H\033[J", end="")

        print("-- PÄÄVALIKKO --\n")
        print("[1] ALOITA PELI")
        print("[2] PELIN OHJEET")
        print("[3] Pelaajan tiedot")
        print("[4] Kerro lempipelisi")
        print("[5] Kerro muuta tietoa itsestäsi")
        print("\n[LOPETA] Sammuta peli")

        pyydetty_toiminto = input("\nValinta: ")

        if pyydetty_toiminto.lower() == "lopeta":
            print("\nPeli sulkeutuu.\n")
            exit()

        try:
            pyydetty_toiminto = int(pyydetty_toiminto)
        except ValueError:
            input("\nVirheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")
            continue

        if pyydetty_toiminto == 1:
            return
        elif pyydetty_toiminto == 2:
            print("\033[H\033[J", end="")

            with open("ohjeet.txt", "r", encoding="utf-8") as tiedosto:
                print(tiedosto.read())

            input("\nPaina [Enter] jatkaaksesi.")
        elif pyydetty_toiminto == 3:
            tulosta_tiedot(tietolista)
        elif pyydetty_toiminto == 4:
            tietolista[2] = lempi_peli()
        elif pyydetty_toiminto == 5:
            tietolista[3] = muu_tieto()
        else:
            input("\nNumerolla ei löytynyt toimintoa.\nPaina [Enter] jatkaaksesi.")

def tulosta_tiedot(tietolista):

    print("\033[H\033[J", end="")
    print("- PELAAJAN TIEDOT -\n")
    print("Nimi:", tietolista[0])
    print("Ikä:", tietolista[1])

    if tietolista[2] != "":
        print("Lempipelisi:", tietolista[2])

    if tietolista[3] != "":
        print("Muuta tietoa sinusta:", tietolista[3])

    input("\n\nPaina [Enter] jatkaaksesi.")

def lempi_peli():

    print("\033[H\033[J", end="")
    lempipeli = input("Kerro lempipelisi: ")

    return lempipeli

def muu_tieto():

    print("\033[H\033[J", end="")
    tieto = input("Kerro muuta tietoa itsestäsi: ")

    return tieto