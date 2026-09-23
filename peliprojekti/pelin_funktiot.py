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
    return

    # tila = pelaaja.sijainti

    # print(f"Tilasta {tila} voi liikkua paikkoihin:")
    # for tila in tila.yhteydet:
    #     print(tila)

    # while True:
    #     try:
    #         print("Minne haluat liikkua?")
    #         print(f"[1] {tila.yhteydet[1]}\n[2] {tila.yhteydet[2]}\n[3] {tila.yhteydet[3]}\n[0] Peruuta")

    #         valinta = int(input("Valinta: "))

    #     except ValueError:
    #         print("Virheellinen valinta, yritä uudelleen.\nPaina [Enter] jatkaaksesi.")
    #         continue

    #     if valinta == 0:
    #         return

    #     elif valinta == 1:
    #         print(f"Siirrytään tilaan {tila.yhteydet[1]}.")
    #         pelaaja.liiku_seuraavaan_paikkaan(tila.yhteydet[1])

    #     elif valinta == 1:
    #         print(f"Siirrytään tilaan {tila.yhteydet[2]}.")
    #         pelaaja.liiku_seuraavaan_paikkaan(tila.yhteydet[2])

    #     elif valinta == 1:
    #         print(f"Siirrytään tilaan {tila.yhteydet[3]}.")
    #         pelaaja.liiku_seuraavaan_paikkaan(tila.yhteydet[3])
        

def ota_esine(pelaaja, esine):

    pelaaja.esineet.append(esine)
    pelaaja.sijainti.esineet.remove(esine)
    print(f"Otit esineen {esine}.")
    

def myy_esine_tai_palauta_pullo(pelaaja):
    return

def osta_tuote(pelaaja):
    return

def syö_tuote(pelaaja):
    return

def tee_töitä_tai_auta(pelaaja):
    return

def ravintolan_menu(pelaaja):
    return

def kaupan_hinnasto(pelaaja):
    return