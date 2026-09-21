from pelin_luokat import Pelaaja, Tila, Esine, Tuote
from pelin_funktiot import mikä_tarinateksti

# Funktio, joka aloittaa pelin, ja luo siihen kuuluvat oliot
def aloita_peli(pelaajan_nimi):

# Luodaan pelin tilat ja alueet
    Koti = Tila("Koti")
    Matka_Ruokakauppaan = Tila("Matka ruokakauppaan")
    Ruokakauppa = Tila("Ruokakauppa")
    Matka_Ravintolaan = Tila("Matka ravintolaan")
    Ravintola = Tila("Ravintola")
    Salainen_Tunneli = Tila("Salainen tunneli")

# Luodaan pelaajaolio
    pelaaja = Pelaaja(pelaajan_nimi, Koti)

# Luodaan pelin esineet
    Palautuspullo_Koti = Esine("Palautuspullo", 0.20)
    Palautuspullo_Matka_Ruokakauppaan = Esine("Palautuspullo", 0.20)
    Palautuspullo_Matka_Ravintolaan = Esine("Palautuspullo", 0.20)
    Lippis = Esine("Lippis", 5)
    Kultaharkko = Esine("Kultaharkko", 1000)

# Luodaan pelin tuotteet
    Omena = Tuote("Omena", 0.50)
    Leipä = Tuote("Leipä", 1)
    Pitsa = Tuote("Pitsa", 4)

# Ajetaan esille pelin päävalikko
    pelivalikko(pelaaja)


def pelivalikko(pelaaja):
    arvo = 1
    
    while True:
        mikä_tarinateksti(arvo)
        while True:
            try:
                valinta = int(input("\nMitä teet?\n> "))
                break
            except ValueError:
                print("Virheellinen valinta! Yritä uudelleen.")

        if valinta == 1:
            print(f"Siirrytään huoneeseen ??")
            arvo += 1
        elif valinta == 2:
            print(f"Etsitään huone...")
        elif valinta == 3:
            print(f"Otetaan esine inventaarioon.")

aloita_peli("Lauri")