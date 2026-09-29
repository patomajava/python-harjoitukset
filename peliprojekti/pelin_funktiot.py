import time



def tulosta_tilanne(pelaaja):

    print("-- PELIN TILANNE --\n")

    print(f"Sijainti: {pelaaja.sijainti.nimi}")
    pelaaja.kello()
    print(f"Nälkä: {pelaaja.nälkä:.0f}/100")
    print(f"Saldo: {pelaaja.raha:.2f} Euroa")


def näytä_esineet_ja_tuotteet(pelaaja):

    print("\033[H\033[J", end="")
    print("- REPUN SISÄLTÖ -")

    print("\nEsineet:")

    if pelaaja.esineet:
        for esine in pelaaja.esineet:
            print(esine.nimi)
    else:
        print("Ei esineitä.")

    print("\nRuoat:")

    if pelaaja.tuotteet:
        for tuote in pelaaja.tuotteet:
            print(tuote.nimi)
    else:
        print("Ei ruokia.")

    input("\nPaina [Enter] jatkaaksesi.")


def tutki_tilaa(pelaaja):

    tila = pelaaja.sijainti

    print("\033[H\033[J", end="")
    print(f"Tutkitaan paikkaa {tila.nimi}...\n")
    pelaaja.ajankulu(30)
    time.sleep(2)

    if not tila.esineet:
        print("Täältä ei löytynyt mitään.")
        input("\nPaina [Enter] jatkaaksesi.")
        return 

    print("Löysit:\n")

    for i in range(len(tila.esineet)):
        esine = tila.esineet[i]
        print(f"{esine.nimi}")

    print("\n-------------------\n")
    print(f"\n[1] Ota {esine.nimi} reppuun")
    print("[0] Peruuta")

    while True:
        try:
            valinta = int(input("\nValinta: "))
            break
        except ValueError:
            input("\nVirheellinen valinta.\nPaina [Enter] jatkaaksesi.")

    if valinta == 0:
        return

    if valinta < 1 or valinta > len(tila.esineet):
        input("\nTuolla numerolla ei löytynyt esinettä.\nPaina [Enter] jatkaaksesi.")
        return

    esine = tila.esineet[valinta - 1]

    ota_esine(pelaaja, esine)


def vaihda_tilaa(pelaaja):

    print("\033[H\033[J", end="")

    tila = pelaaja.sijainti
    yhteydet = list(tila.yhteydet.values())

    print("Mihin haluat liikkua?\n")

    for i in range(len(yhteydet)):
        print(f"[{i + 1}] {yhteydet[i].nimi}")

    print("\n[0] Peruuta")

    while True:
        try:
            valinta = int(input("\nValinta: "))
            break
        except ValueError:
            input("\nVirheellinen valinta.\nPaina [Enter] jatkaaksesi.")

    if valinta == 0:
        return

    if valinta < 1 or valinta > len(yhteydet):
        input("\nTuolla numerolla ei löytynyt paikkaa.\nPaina [Enter] jatkaaksesi.")
        return

    uusi_tila = yhteydet[valinta - 1]

    pelaaja.liiku_seuraavaan_paikkaan(uusi_tila)
    pelaaja.ajankulu(30)


def ota_esine(pelaaja, esine):

    pelaaja.ota_esine(esine)
    pelaaja.sijainti.esineet.remove(esine)

    print(f"\n{esine.nimi} on nyt repussasi.")
    input("Paina [Enter] jatkaaksesi.")


def myy_esine(pelaaja):

    print("\033[H\033[J", end="")

    if not pelaaja.esineet:
        print("Sinulla ei ole myytäviä esineitä.")
        input("Paina [Enter] jatkaaksesi.")
        return

    print("- MYYTÄVÄT ESINEET -")

    for i in range(len(pelaaja.esineet)):
        esine = pelaaja.esineet[i]
        print(f"\n[{i + 1}] {esine.nimi}\nArvo: {esine.arvo:.2f} euroa")

    print("\n[0] Peruuta")

    while True:
        try:
            valinta = int(input("\nValinta: "))
            break
        except ValueError:
            input("Virheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")

    if valinta == 0:
        return

    if valinta < 1 or valinta > len(pelaaja.esineet):
        input("Tuolla numerolla ei löytynyt esinettä.\nPaina [Enter] jatkaaksesi.")
        return

    esine = pelaaja.esineet[valinta - 1]

    pelaaja.raha += esine.arvo
    pelaaja.esineet.remove(esine)
    pelaaja.ajankulu(10)

    print(f"\nMyit esineen {esine.nimi} ja sait {esine.arvo:.2f} euroa.")
    input("\nPaina [Enter] jatkaaksesi.")


def osta_tuote(pelaaja):

    tila = pelaaja.sijainti

    print("\033[H\033[J", end="")
    print("- OSTETTAVAT TUOTTEET -\n")

    for i in range(len(tila.tuotteet)):
        tuote = tila.tuotteet[i]
        print(f"[{i + 1}] {tuote.nimi} - {tuote.hinta:.2f} euroa")

    print("\n[0] Peruuta")

    while True:
        try:
            valinta = int(input("\nValinta: "))
            break
        except ValueError:
            input("\nVirheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")

    if valinta == 0:
        return

    if valinta < 1 or valinta > len(tila.tuotteet):
        input("Tuolla numerolla ei löytynyt tuotetta.\nPaina [Enter] jatkaaksesi.")
        return

    tuote = tila.tuotteet[valinta - 1]

    if pelaaja.raha < tuote.hinta:
        print("\nSinulla ei ole tarpeeksi rahaa.")
        input("Paina [Enter] jatkaaksesi.")
        return

    pelaaja.osta_tuote(tuote)
    pelaaja.ajankulu(10)

    print(f"\nOstit tuotteen {tuote.nimi}.")
    input("Paina [Enter] jatkaaksesi.")


def syö_tuote(pelaaja):

    print("\033[H\033[J", end="")
    print("- RUOAT REPUSSA -\n")

    if not pelaaja.tuotteet:
        print("Sinulla ei ole ruokaa.")
        input("\nPaina [Enter] jatkaaksesi.")
        return

    for i in range(len(pelaaja.tuotteet)):
        tuote = pelaaja.tuotteet[i]
        print(f"[{i + 1}] {tuote.nimi} - Ravintoarvo: {tuote.ravintoarvo}")

    print("\n[0] Peruuta")

    while True:
        try:
            valinta = int(input("\nValinta: "))
            break
        except ValueError:
            input("\nVirheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")

    if valinta == 0:
        return

    if valinta < 1 or valinta > len(pelaaja.tuotteet):
        input("Tuolla numerolla ei löytynyt ruokaa.\nPaina [Enter] jatkaaksesi.")
        return

    tuote = pelaaja.tuotteet[valinta - 1]

    pelaaja.syö(tuote)
    pelaaja.ajankulu(20)

    print(f"\nSöit tuotteen {tuote.nimi}.")
    print(f"Nälkäsi on nyt: {pelaaja.nälkä:.0f}/100")

    input("\nPaina [Enter] jatkaaksesi.")


def tee_töitä(pelaaja):

    print("\033[H\033[J", end="")
    print("- AVUN ANTO -\n")

    print("[1] Auta tiskien tiskaamisessa (5 euroa / tunti)")
    print("[2] Auta lattian siivoamisessa (2 euroa / 30 minuuttia)")
    print("[0] Peruuta")

    while True:
        try:
            valinta = int(input("\nValinta: "))
            break
        except ValueError:
            input("Virheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")

    if valinta == 1:
        pelaaja.raha += 5
        pelaaja.ajankulu(60)
        print("\nTiskasit tunnin ja sait 5 euroa.")

    elif valinta == 2:
        pelaaja.raha += 2
        pelaaja.ajankulu(30)
        print("\nSiivosit lattiaa 30 minuuttia ja sait 2 euroa.")

    elif valinta == 0:
        return

    else:
        print("\nTuolla numerolla ei löytynyt töitä.")

    input("\nPaina [Enter] jatkaaksesi.")


def ravintolan_menu(pelaaja):

    tila = pelaaja.sijainti

    print("\033[H\033[J", end="")
    print("- RAVINTOLAN MENU -\n")

    for tuote in tila.tuotteet:
        print(f"{tuote.nimi}: {tuote.hinta:.2f} euroa")

    input("\nPaina [Enter] jatkaaksesi.")


def kaupan_hinnasto(pelaaja):

    tila = pelaaja.sijainti

    print("\033[H\033[J", end="")
    print("- KAUPAN HINNASTO -\n")

    for tuote in tila.tuotteet:
        print(f"{tuote.nimi}: {tuote.hinta:.2f} euroa")

    input("\nPaina [Enter] jatkaaksesi.")