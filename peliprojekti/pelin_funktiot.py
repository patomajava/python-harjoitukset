def tulosta_tilanne(pelaaja):
    print("-- PELIN TILANNE --\n")

    print(f"Sijainti: {pelaaja.sijainti.nimi}")
    pelaaja.kello()
    print(f"Nälkä: {pelaaja.nälkä}/100")
    print(f"Saldo: {pelaaja.raha} Euroa")


def näytä_esineet_ja_tuotteet(pelaaja):

    print("\033[H\033[J", end="")

    print("- REPUN SISÄLTÖ -")

    print("\nEsineet:")
    for esine in pelaaja.esineet:
        print(esine.nimi)

    print("\nRuoat:")
    for tuote in pelaaja.tuotteet:
        print(tuote.nimi)

    input("\n\nPaina [Enter] jatkaaksesi.")
    

def tutki_tilaa(pelaaja):

    tila = pelaaja.sijainti

    print(f"Tutkitaan paikkaa {tila.nimi}...")
    print("Löysit:")

    for esine in tila.esineet:
        print(esine.nimi)

    input("Paina [Enter] jatkaaksesi.")

    return tila.esineet


def vaihda_tilaa(pelaaja):
    tila = pelaaja.sijainti
    yhteydet = list(tila.yhteydet.values())

    print("Mihin haluat liikua?")

    print(f"[1] {yhteydet[0].nimi}")
    print(f"[2] {yhteydet[1].nimi}")

    try:
        valinta = int(input("Valinta: "))
    except ValueError:
        print("Virheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")

    if valinta == 1:
        pelaaja.liiku_seuraavaan_paikkaan(yhteydet[0])
    elif valinta == 2:
        pelaaja.liiku_seuraavaan_paikkaan(yhteydet[1])

        
def ota_esine(pelaaja, esine):

    pelaaja.ota_esine(esine)
    pelaaja.sijainti.esineet.remove(esine)
    print(f"Otit esineen {esine.nimi}.")

    
def myy_esine_tai_palauta_pullo(pelaaja):
    tila = pelaaja.sijainti

    if tila.nimi == "Ruokakauppa":
        pelaaja.esineet.remove()

    if tila.nimi == "Ravintola":
        pelaaja.esineet.remove()


def osta_tuote(pelaaja):
    tila = pelaaja.sijainti

    print("- OSTETTAVAT TUOTTEET -\n")
    for tuote in tila.tuotteet:
        print(tuote.nimi)

    print("Minkä tuotteen haluat ostaa?")

    try:
        valinta = int(input("Valinta: "))
    except ValueError:
        print("Virheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")

    if valinta == 1:
        tuote = tila.tuotteet[0]
    elif valinta == 2:
        tuote = tila.tuotteet[1]
    elif valinta == 3:
        tuote = tila.tuotteet[2]

    if pelaaja.raha >= tuote.hinta:
        pelaaja.osta_tuote(tuote)
        print(f"Ostit tuotteen {tuote.nimi}.")
    else:
        print("Sinulla ei ole tarpeeksi rahaa.")

    input("Paina [Enter] jatkaaksesi.")


def syö_tuote(pelaaja):
    print("- RUOAT REPUSSA -\n")
    for tuote in pelaaja.tuotteet:
        print(tuote.nimi)

    print("\nMinkä ruoan haluat syödä? 1/2")

    try:
        valinta = int(input("\nValinta: "))
    except ValueError:
        print("Virheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")

    if valinta == 1:
        tuote = pelaaja.tuotteet[0]
    elif valinta == 2:
        tuote = pelaaja.tuotteet[1]
    elif valinta == 3:
        tuote = pelaaja.tuotteet[2]


    pelaaja.syö(tuote)
    print(f"Söit tuotteen {tuote}.")


def tee_töitä(pelaaja):
    print("- AVUN ANTO VALIKKO -\n")

    print("Auta tiskien tiskaamisessa (5e/h)")
    print("Auta lattian siivoamisessa (2e/30min)")


def ravintolan_menu(pelaaja):
    tila = pelaaja.sijainti

    print("- RAVINTOLAN MENU -\n")
    for tuote in tila.tuotteet:
        print(f"{tuote.nimi}: Hinta: {tuote.hinta} euroa.")


def kaupan_hinnasto(pelaaja):
    tila = pelaaja.sijainti

    print("- KAUPAN HINNASTO -\n")
    for tuote in tila.tuotteet:
        print(f"{tuote.nimi}: Hinta: {tuote.hinta} euroa.")