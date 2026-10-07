from pelin_luokat import Pelaaja, Tila, Esine, Tuote
from pelin_funktiot import pelin_kartta, tulosta_tilanne, näytä_esineet_ja_tuotteet, tutki_tilaa, vaihda_tilaa, myy_esine, osta_tuote, syö_tuote, ravintolan_menu, kaupan_hinnasto, tee_töitä
from tarinatekstit import pelin_intro
from tallennus import tallenna_peli

def luodaan_pelin_maailma():

# LUODAAN PELIN TILAT JA ALUEET.
    koti = Tila("Koti")
    pihatie = Tila("Pihatie")
    puisto = Tila("Puisto")
    merenranta = Tila("Merenranta")
    metsä = Tila("Metsä")
    ruokakauppa = Tila("Ruokakauppa")
    ravintola = Tila("Ravintola")
    kirpputori = Tila("Kirpputori")
    salainen_kellari = Tila("Salainen kellari")

# LUODAAN PELIN ESINEET | ESINEET OVAT ASIOITA JOITA PELAAJA VOI MYYDÄ
    avaimenperä = Esine("Avaimenperä", 3)
    hieno_kivi = Esine("Hieno kivi", 1)
    lippis = Esine("Lippis", 6)
    kultaharkko = Esine("Kultaharkko", 500)

    metsä.lisää_esine(hieno_kivi)
    pihatie.lisää_esine(avaimenperä)
    puisto.lisää_esine(lippis)
    salainen_kellari.lisää_esine(kultaharkko)

# LUODAAN PELIN TUOTTEET | TUOTTEET OVAT ASIOITA JOITA PELAAJA VOI OSTAA
    omena = Tuote("Omena", 0.50, 10)
    leipä = Tuote("Leipä", 1, 20)
    pitsa = Tuote("Pitsa", 4, 50)

    kebabrulla = Tuote("Kebabrulla", 8, 60)
    kebab_ranskalaisilla = Tuote("Kebab Ranskalaisilla", 8, 60)
    sisäfileepihvi = Tuote("Sisäfileepihvi", 100, 90)

    ruokakauppa.lisää_tuote(omena)
    ruokakauppa.lisää_tuote(leipä)
    ruokakauppa.lisää_tuote(pitsa)

    ravintola.lisää_tuote(kebabrulla)
    ravintola.lisää_tuote(kebab_ranskalaisilla)
    ravintola.lisää_tuote(sisäfileepihvi)


# LUODAAN TILOILLE YHTEYDET TOISIIN TILOIHIN
    koti.lisää_yhteys("Pihatie", pihatie)

    salainen_kellari.lisää_yhteys("Koti", koti)

    pihatie.lisää_yhteys("Koti", koti)
    pihatie.lisää_yhteys("Puisto", puisto)
    pihatie.lisää_yhteys("Metsä", metsä)

    puisto.lisää_yhteys("Pihatie", pihatie)
    puisto.lisää_yhteys("Metsä", metsä)
    puisto.lisää_yhteys("Ruokakauppa", ruokakauppa)
    puisto.lisää_yhteys("Ravintola", ravintola)
    puisto.lisää_yhteys("Kirpputori", kirpputori)

    metsä.lisää_yhteys("Merenranta", merenranta)
    metsä.lisää_yhteys("Puisto", puisto)
    metsä.lisää_yhteys("Pihatie", pihatie)

    merenranta.lisää_yhteys("Metsä", metsä)

    ruokakauppa.lisää_yhteys("Puisto", puisto)
    ruokakauppa.lisää_yhteys("Ravintola", ravintola)
    ruokakauppa.lisää_yhteys("Kirpputori", kirpputori)

    ravintola.lisää_yhteys("Puisto", puisto)
    ravintola.lisää_yhteys("Ruokakauppa", ruokakauppa)
    ravintola.lisää_yhteys("Kirpputori", kirpputori)

    kirpputori.lisää_yhteys("Puisto", puisto)
    kirpputori.lisää_yhteys("Ravintola", ravintola)
    kirpputori.lisää_yhteys("Ruokakauppa", ruokakauppa)

    kaikki_tilat = {"Koti": koti, "Salainen kellari": salainen_kellari, "Pihatie": pihatie, "Puisto": puisto, "Metsä": metsä, "Merenranta": merenranta, "Ruokakauppa": ruokakauppa, "Ravintola": ravintola, "Kirpputori": kirpputori}

    return kaikki_tilat

def lataa_pelaaja(tiedot):

    kaikki_tilat = luodaan_pelin_maailma()
    sijainti = kaikki_tilat[tiedot["sijainti"]]
    pelaaja = Pelaaja(tiedot["nimi"], int(tiedot["ikä"]), sijainti)
    pelaaja.salainen_kellari = kaikki_tilat["Salainen kellari"]

    pelaaja.nälkä = float(tiedot["nälkä"])
    pelaaja.raha = float(tiedot["raha"])
    pelaaja.aika = int(tiedot["aika"])

    pelaaja.koti_kerrat = int(tiedot["koti_kerrat"])
    pelaaja.salainen_kellari_avattu = tiedot["salainen_kellari_avattu"] == "True"

    if tiedot["pelaajan_esineet"]:
        for esineen_tieto in tiedot["pelaajan_esineet"].split("|"):
            nimi, arvo = esineen_tieto.split(":")

            esine = Esine(nimi, int(arvo))
            pelaaja.esineet.append(esine)

    if tiedot["pelaajan_tuotteet"]:
        for tuotteen_tieto in tiedot["pelaajan_tuotteet"].split("|"):
            nimi, hinta, ravintoarvo = tuotteen_tieto.split(":")

            tuote = Tuote(nimi, float(hinta), int(ravintoarvo))
            pelaaja.tuotteet.append(tuote)

    for nimi, tila in kaikki_tilat.items():

        avain = f"tila_{nimi}_esineet"
        if avain not in tiedot:
            continue
        tila.esineet.clear()

        if tiedot[avain]:
            for esineen_tieto in tiedot[avain].split("|"):
                nimi, arvo = esineen_tieto.split(":")
                esine = Esine(nimi, int(arvo))
                tila.esineet.append(esine)

    if pelaaja.salainen_kellari_avattu == True:

        koti = kaikki_tilat["Koti"]
        if "Salainen kellari" not in koti.yhteydet:
            koti.lisää_yhteys("Salainen kellari", pelaaja.salainen_kellari)

    return pelaaja, kaikki_tilat

def pelivalikko(pelaaja, kaikki_tilat):

    while True:
        print("\033[H\033[J", end="")

        if pelaaja.nälkä >= 100:
            print("Nälkätaso on liian korkea, HÄVISIT PELIN.")
            input("\nPaina [Enter] jatkaaksesi.")
            return

        if pelaaja.aika >= 1200:
            print("Päivä päättyi.\n")

            if pelaaja.nälkä <= 40:
                print("Sait syötyä tarpeeksi, VOITIT PELIN.")
            else:
                print("Et saanut syötyä tarpeeksi, HÄVISIT PELIN.")

            input("\nPaina [Enter] jatkaaksesi.")
            return

        tulosta_tilanne(pelaaja)

        print("\n--", pelaaja.sijainti.nimi.upper(), "--\n")
        print("Mitä haluat tehdä seuraavaksi?\n")

        print("[1] Liiku")

        if pelaaja.sijainti.nimi == "Ruokakauppa":
            print("[2] Näytä hinnasto")
            print("[3] Osta tuote")
            print("[4] Näytä reppu")
            print("[5] Syö ruokaa")

        elif pelaaja.sijainti.nimi == "Ravintola":
            print("[2] Näytä menu")
            print("[3] Tilaa ruokaa")
            print("[4] Auta henkilökuntaa")
            print("[5] Näytä reppu")
            print("[6] Syö ruokaa")

        elif pelaaja.sijainti.nimi == "Kirpputori":
            print("[2] Osta vihje - 4 euroa")
            print("[3] Myy tavaraa")
            print("[4] Näytä reppu")
            print("[5] Syö ruokaa")

        else:
            print("[2] Tutki ympäristöä")
            print("[3] Näytä reppu")
            print("[4] Syö ruokaa")
            print("[5] Näytä kartta")

        print("\n[POISTU] Poistu pelistä")

        valinta = input("\nValinta: ")

        if valinta.lower() == "poistu":
            tallenna_peli(pelaaja, kaikki_tilat)

            input("\nPeli tallennettu.\nPaina [Enter] jatkaaksesi.")
            return

        try:
            valinta = int(valinta)
        except ValueError:
            input("\nVirheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")
            continue

        if valinta == 1:
            vaihda_tilaa(pelaaja)
        elif pelaaja.sijainti.nimi == "Ruokakauppa" and valinta == 2:
            kaupan_hinnasto(pelaaja)
        elif pelaaja.sijainti.nimi == "Ruokakauppa" and valinta == 3:
            osta_tuote(pelaaja)
        elif pelaaja.sijainti.nimi == "Ruokakauppa" and valinta == 4:
            näytä_esineet_ja_tuotteet(pelaaja)
        elif pelaaja.sijainti.nimi == "Ruokakauppa" and valinta == 5:
            syö_tuote(pelaaja)
        elif pelaaja.sijainti.nimi == "Ravintola" and valinta == 2:
            ravintolan_menu(pelaaja)
        elif pelaaja.sijainti.nimi == "Ravintola" and valinta == 3:
            osta_tuote(pelaaja)
        elif pelaaja.sijainti.nimi == "Ravintola" and valinta == 4:
            tee_töitä(pelaaja)
        elif pelaaja.sijainti.nimi == "Ravintola" and valinta == 5:
            näytä_esineet_ja_tuotteet(pelaaja)
        elif pelaaja.sijainti.nimi == "Ravintola" and valinta == 6:
            syö_tuote(pelaaja)
        elif pelaaja.sijainti.nimi == "Kirpputori" and valinta == 2:
            if pelaaja.raha - 4 < 0:
                print("Sinulla ei ole tarpeeksi rahaa")
            else:
                pelaaja.raha -= 4
                print("\nVihje: Joskus lähtötilanteesta voi löytyä jotain uutta, mitä ei ehkä odottanutkaan.")
                input("Paina [Enter] jatkaaksesi.")
        elif pelaaja.sijainti.nimi == "Kirpputori" and valinta == 3:
            myy_esine(pelaaja)
        elif pelaaja.sijainti.nimi == "Kirpputori" and valinta == 4:
            näytä_esineet_ja_tuotteet(pelaaja)
        elif pelaaja.sijainti.nimi == "Kirpputori" and valinta == 5:
            syö_tuote(pelaaja)
        elif valinta == 2:
            tutki_tilaa(pelaaja)
        elif valinta == 3:
            näytä_esineet_ja_tuotteet(pelaaja)
        elif valinta == 4:
            syö_tuote(pelaaja)
        elif valinta == 5:
            pelin_kartta()
        else:
            input("\nNumerolla ei löytynyt toimintoa.\nPaina [Enter] jatkaaksesi.")

def aloita_peli(pelaaja, kaikki_tilat):

    print("\033[H\033[J", end="")
    pelin_intro()
    input("\nPaina [Enter] aloittaaksesi pelin.")

    pelivalikko(pelaaja, kaikki_tilat)

    return