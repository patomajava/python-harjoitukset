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