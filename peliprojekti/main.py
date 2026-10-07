import os
from päävalikko import pelaajan_tiedot, päävalikko
from peli import luodaan_pelin_maailma, lataa_pelaaja, aloita_peli
from pelin_luokat import Pelaaja
from tallennus import lataa_peli

# MUUTETAAN HAKEMISTO JOTTA TIEDOSTOT TOIMIVAT OIKEIN.
os.chdir(os.path.dirname(__file__))

# AVATAAN JA LUETAAN PELIN ALOITUSTEKSTI.
with open("intro.txt", "r", encoding="utf-8") as tiedosto:
    input(tiedosto.read() + "\n\nPaina [Enter] aloittaaksesi pelin.")

# TÄLLÄ LAUSEELLA TYHJENNETÄÄN TERMINAALI.
print("\033[H\033[J", end="")

# YRITETÄÄN LADATA AIEMPI TALLENNUS.
tallennus = lataa_peli()

if tallennus is not None:

    print("-- TALLENNETTU PELI LÖYTYI --\n")

    while True:

        print("[1] Jatka peliä")
        print("[2] Aloita uusi peli")

        while True:
            try:
                valinta = int(input("\nValinta: "))
                break
            except ValueError:
                input("\nVirheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")

        if valinta == 1:
            # LADATAAN PELAAJA JA PELIMAAILMA TALLENNUSTIEDOSTOSTA
            pelaaja, kaikki_tilat = lataa_pelaaja(tallennus)
            break
        elif valinta == 2:
            # LUODAAN KOKONAAN UUSI PELI
            print("\033[H\033[J", end="")
            pelaajan_nimi, pelaajan_ikä = pelaajan_tiedot()
            kaikki_tilat = luodaan_pelin_maailma()

            pelaaja = Pelaaja(pelaajan_nimi, pelaajan_ikä, kaikki_tilat["Koti"])
            pelaaja.salainen_kellari = kaikki_tilat["Salainen kellari"]
            break
        else: 
            input("\nVirheellinen valinta.\nPaina [Enter] jatkaaksesi.")
else:
# TALLENNUSTA EI OLLUT, JOTEN LUODAAN UUSI PELI
    pelaajan_nimi, pelaajan_ikä = pelaajan_tiedot()

    kaikki_tilat = luodaan_pelin_maailma()

    pelaaja = Pelaaja(pelaajan_nimi, pelaajan_ikä, kaikki_tilat["Koti"])
    pelaaja.salainen_kellari = kaikki_tilat["Salainen kellari"]
    
# AJETAAN PÄÄVALIKON JA PELIVALIKON LOPUTON SILMUKKA.
while True:

    tietolista = [pelaaja.nimi, pelaaja.ikä, "", ""]
    päävalikko(tietolista)
    aloita_peli(pelaaja, kaikki_tilat)