from pelin_luokat import Pelaaja, Huone, Esine

# Funktio, joka ajetaan kun peli alkaa. Kertoo alun tarinan ja kysyy pelaajalta ensimmäisen suunnan.
def ensimmäinen_valikko():

    print("\n\nTervetuloa pelaamaan peliä!\n\n")
    print("Olet juuri herännyt, kello on 8:00 ja olet nälkäinen. Lähdet etsimään ruokaa keittiöstä. Avaat jääkaapin, mutta se on tyhjä. Avaat pakastimen, mutta sekin on tyhjä. Käyt koko keittiön läpi mutta kaapeista ei löydy mitään.\n")
    print("Sinun täytyy nyt lähteä etsimään ruokaa, mutta mistä?\n")

    ensimmäinen_suunta = 0

    try:
        ensimmäinen_suunta = int(input("1. Lähdet ruokakauppaan, johon on pitkä matka, mutta siellä hinnat ovat halpoja.\n2. Lähdet lähimpään Kebab-ravintolaan, se ei ole yhtä kaukana kuin ruokakauppa, mutta siellä hinnat ovat kalliimpia.\n3. Mietit, pitäisikö sinun tutkia vielä, löytyykö talostasi mitään, mikä voisi olla matkallesi hyödyllistä...\n\nMinkä vaihtoehdon valitset: "))
    except ValueError:
        print("Virheellinen valinta, palataan päävalikkoon.")

    if ensimmäinen_suunta == 1:
        seuraava_paikka("Ruokakauppa")
    elif ensimmäinen_suunta == 2:
        seuraava_paikka("Kebab-ravintola")
    elif ensimmäinen_suunta == 3:
        seuraava_paikka("Oma koti")
    elif ensimmäinen_suunta != 1 or 2 or 3:
        print("Tuolla numerolla ei löytynyt vaihtoehtoa.")

# Funktio, jota voidaan kutsua aina kun pelaaja siirtyy edellisestä huoneesta seuraavaan.
def seuraava_paikka(pelaaja, nykyinen_huone, uusi_huone):
    huone = Huone(uusi_huone)
    print(f"{pelaaja} siirtyy paikasta {nykyinen_huone} paikkaan {uusi_huone}")
    return huone

# Funktio, jota voidaan kutsua aina kun pelaaja tahtoo ottaa esineen itselleen.
def keraa_esine(pelaaja, esine):
    pelaaja.esineet.append()
    print(pelaaja.esineet)
    print(f"Olet kerännyt esineen {esine}.")
    return

def liiku(huoneen_nimi):
    print((f"Olet siirtymässä paikkaan {huoneen_nimi}."))
    seuraava_paikka(huoneen_nimi)
    return


def pelivalikko():
    return