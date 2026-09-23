from pelin_luokat import Pelaaja, Tila, Esine, Tuote
from pelin_funktiot import tulosta_tilanne, näytä_esineet_ja_tuotteet, tutki_tilaa, vaihda_tilaa, ota_esine, myy_esine_tai_palauta_pullo, osta_tuote, syö_tuote, ravintolan_menu, kaupan_hinnasto, tee_töitä_tai_auta
from tarinatekstit import pelin_intro
import time

  
# FUNKTIO, Joka luo pelimaailman kaikki oliot, ja lisää olioihin tarvittavat tiedot. Funktio palauttaa arvon "koti", koska pelaajaolio tarvitsee aloitustilan "aloita_peli" Funktiossa.
def luodaan_pelin_maailma():

# LUODAAN PELIIN TILAT JA ALUEET.
    koti = Tila("Koti")
    matka_ruokakauppaan = Tila("Matka ruokakauppaan")
    ruokakauppa = Tila("Ruokakauppa")
    matka_ravintolaan = Tila("Matka ravintolaan")
    ravintola = Tila("Ravintola")
    matka_kotiin = Tila("Matka kotiin")
    salainen_tunneli = Tila("Salainen tunneli")

# LUODAAN PELIIN ESINEET | ESINEET OVAT ASIOITA JOITA PELAAJA VOI MYYDÄ, MUTTA EI SYÖDÄ TAI KÄYTTÄÄ.
    palautuspullo_koti = Esine("Palautuspullo", 0.20)
    palautuspullo_matka_ruokakauppaan = Esine("Palautuspullo", 0.20)
    palautuspullo_matka_ravintolaan = Esine("Palautuspullo", 0.20)
    lippis = Esine("Lippis", 5)
    kultaharkko = Esine("Kultaharkko", 1000)

# LISÄTÄÄN ESINEET OIKEISIIN TILOIHIN
    koti.lisää_esine(palautuspullo_koti)

    matka_ruokakauppaan.lisää_esine(palautuspullo_matka_ruokakauppaan)
    matka_ravintolaan.lisää_esine(palautuspullo_matka_ravintolaan)

    matka_kotiin.lisää_esine(lippis)
    salainen_tunneli.lisää_esine(kultaharkko)

# LUODAAN PELIN TUOTTEET | TUOTTEET OVAT ASIOITA JOITA PELAAJA VOI SYÖDÄ TAI KÄYTTÄÄ, MUTTA EI MYYDÄ.
    omena = Tuote("Omena", 0.50, 10)
    leipä = Tuote("Leipä", 1, 20)
    pitsa = Tuote("Pitsa", 4, 50)

    kebabrulla = Tuote("Kebabrulla", 8, 60)
    kebab_ranskalaisilla = Tuote("Kebab ranskalaisilla", 8, 60)
    sisäfileepihvi = Tuote("Sisäfileepihvi", 100, 90)

# LISÄTÄÄN TUOTTEET OIKEISIN TILOIHIN
    ruokakauppa.lisää_tuote(omena)
    ruokakauppa.lisää_tuote(leipä)
    ruokakauppa.lisää_tuote(pitsa)

    ravintola.lisää_tuote(kebabrulla)
    ravintola.lisää_tuote(kebab_ranskalaisilla)
    ravintola.lisää_tuote(sisäfileepihvi)

# LISÄTÄÄN TILOILLE YHTEYDET TOISIIN TILOIHIN

    koti.lisää_yhteys = "Matka ruokakauppaan", matka_ruokakauppaan
    koti.lisää_yhteys = "Matka ravintolaan", matka_ravintolaan

    matka_ruokakauppaan.lisää_yhteys("Koti", koti)
    matka_ruokakauppaan.lisää_yhteys("Ruokakauppa", ruokakauppa)
    matka_ruokakauppaan.lisää_yhteys("Matka ravintolaan", matka_ravintolaan)

    matka_ravintolaan.lisää_yhteys("Koti", koti)
    matka_ravintolaan.lisää_yhteys("Ravintola", ravintola)
    matka_ravintolaan.lisää_yhteys("Matka ruokakauppaan", ravintola)

    ruokakauppa.lisää_yhteys("Matka ravintolaan", matka_ravintolaan)
    ruokakauppa.lisää_yhteys("Matka kotiin", matka_kotiin)

    ravintola.lisää_yhteys("Matka ruokakauppaan", matka_ruokakauppaan)
    ravintola.lisää_yhteys("Matka kotiin", matka_kotiin)

    matka_kotiin.lisää_yhteys("Matka ruokakauppaan", matka_ruokakauppaan)
    matka_kotiin.lisää_yhteys("Matka ravintolaan", matka_ravintolaan)
    matka_kotiin.lisää_yhteys("Koti", koti)

    return koti


# FUNKTIO, Joka tulostuu kun pelaaja avaa pelivalikosta tilakohtaisen valikon. Toinen valikko tehty ettei pelivalikossa ole liian montaa vaihtoehtoa päällekäin, tehden siitä sekavaisemman, kuin olisi tarve.
def tilan_valikko(pelaaja):
    
    while True:
        print("\033[H\033[J", end="")

        print(f"- {pelaaja.sijainti.nimi.upper()}-TILAN VALIKKO -\n")
        print("Mitä haluat tehdä seuraavaksi?\n")
        print("[1] Palaa takaisin pelin valikkoon")

        if pelaaja.sijainti.nimi == "Matka Ruokakauppaan" or pelaaja.sijainti.nimi == "Matka Ravintolaan":
            print("[2] Tutki ympäristöä")

        if pelaaja.sijainti.nimi == "Ruokakauppa":
            print("[2] Näytä kaupan hinnasto")
            print("[3] Osta jokin tuote")
            print("[4] Auta henkilökuntaa")
            print("[5] Palauta pulloja")

        if pelaaja.sijainti.nimi == "Ravintola":
            print("[2] Näytä ravintolan menu")
            print("[3] Tilaa ruokaa")
            print("[4] Auta henkilökuntaa")
            print("[5] Myy tavaraa")

        try:
            valinta = int(input("\nValinta: "))
        except ValueError:
            print("\nVirheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")
            continue

        if valinta == 1:
            return
        
        elif valinta == 2 and (pelaaja.sijainti.nimi == "Matka Ruokakauppaan" or valinta == 2 and pelaaja.sijainti.nimi == "Matka Ravintolaan"):
            tilan_asiat = tutki_tilaa(pelaaja)

            if tilan_asiat != "":
                valinta = input("Haluatko ottaa esineen reppuusi? [kyllä/ei]")

                if valinta.lower() == "kyllä":
                    for esine in tilan_asiat:
                        ota_esine(pelaaja, esine)
                elif valinta.lower() == "ei":
                    print("Selvä, ei oteta esineitä mukaan")

        elif valinta == 2 and pelaaja.sijainti.nimi == "Ruokakauppa":
            kaupan_hinnasto(pelaaja)

        elif valinta == 2 and pelaaja.sijainti.nimi == "Ravintola":
            ravintolan_menu(pelaaja)

        elif valinta == 3 and pelaaja.sijainti.nimi == "Ruokakauppa" or valinta == 3 and pelaaja.sijainti.nimi == "Ravintola":
            osta_tuote(pelaaja)

        elif valinta == 4 and pelaaja.sijainti.nimi == "Ruokakauppa" or valinta == 3 and pelaaja.sijanti.nimi == "Ravintola":
            tee_töitä_tai_auta(pelaaja)

        elif valinta == 5 and pelaaja.sijainti.nimi == "Ruokakauppa" or valinta == 5 and pelaaja.sijainti.nimi == "Ravintola":
            myy_esine_tai_palauta_pullo(pelaaja)
            


# FUNKTIO, Joka toistaa pelivalikkoa kunnes käyttäjä haluaa palata päävalikkoon. Päävalikko on niinsanottu HUB kaikille pelissä oleville toiminnoille.
def pelivalikko(pelaaja):

    while True:
        print("\033[H\033[J", end="")

        if pelaaja.nälkä >= 100:
            print("Kuolit nälkään LMAO.")
            return
        
        if pelaaja.aika >= 1320:
            print("Päivä päättyi.")

            if pelaaja.nälkä <= 20:
                print("Sait syötyä tarpeeksi, VOITIT PELIN.")

            elif pelaaja.nälkä >= 20:
                print("Et saanut syötyä tarpeeksi, HÄVISIT PELIN.")

            return

        tulosta_tilanne(pelaaja)

        print("\n-- PELIN VALIKKO --\n")
        print("Mitä haluat tehdä seuraavaksi?\n")
        print(f"[1] Näytä '{pelaaja.sijainti.nimi}' Valikko")
        print("[2] Liiku toiseen paikkaan")
        print("[3] Näytä repun sisältö")
        print("[4] Syö ruokaa")
        print("\n[palaa] Palaa päävalikkoon")

        try: 
            valinta = input("\nValinta: ")
            if valinta.lower() == "palaa":
                return
            
            valintaluku = int(valinta) 

        except ValueError:
            input("\nVirheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")
            continue

        if valintaluku == 1:
            tilan_valikko(pelaaja)

        elif valintaluku == 2:
            vaihda_tilaa(pelaaja)

        elif valintaluku == 3:
            näytä_esineet_ja_tuotteet(pelaaja)

        elif valintaluku == 4:
            syö_tuote(pelaaja)
    

# FUNKTIO, Joka ajetaan kun käyttäjä haluaa aloittaa pelin päävalikossa. Ensimmäiseksi Funktio luo pelin kaikki oliot, sekä niiden arvot ja yhteydet. Tämän jälkeen ohjelma luo Pelaajaolion palautetun "koti" olion avulla,
# jonka jälkeen peli tulostaa ensimmäisen tarinatekstin ja käynnistää pelin [Enter] komennosta.
def aloita_peli(pelaajan_nimi):
    aloitustila = luodaan_pelin_maailma()

    pelaaja = Pelaaja(pelaajan_nimi, aloitustila)

    print("\033[H\033[J", end="")

    pelin_intro()
    input("[Enter] Aloita Peli")

    pelivalikko(pelaaja)
    return