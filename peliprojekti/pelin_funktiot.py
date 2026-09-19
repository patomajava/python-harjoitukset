def aloita_peli():
    print("\n\nTervetuloa pelaamaan peliä!\n\n")

    print("Olet juuri herännyt, kello on 8:00 ja olet nälkäinen. Lähdet etsimään ruokaa keittiöstä. Avaat jääkaapin, mutta se on tyhjä. Avaat pakastimen, mutta sekin on tyhjä. Käyt koko keittiön läpi mutta kaapeista ei löydy mitään.\n")

    print("Sinun täytyy nyt lähteä etsimään ruokaa, mutta mistä?\n")

    ensimmäinen_suunta = 0

    try:
        ensimmäinen_suunta = int(input("1. Lähdet ruokakauppaan, johon on pitkä matka, mutta siellä hinnat ovat halpoja.\n2. Lähdet lähimpään Kebab-ravintolaan, se ei ole yhtä kaukana kuin ruokakauppa, mutta siellä hinnat ovat kalliimpia.\n3. Mietit, pitäisikö sinun tutkia vielä, löytyykö talostasi mitään, mikä voisi olla matkallesi hyödyllistä...\n\nMinkä vaihtoehdon valitset: "))
    except ValueError:
        print("Virheellinen valinta, palataan päävalikkoon.")

    if ensimmäinen_suunta == 1:
        print("Ruokakauppa")
    elif ensimmäinen_suunta == 2:
        print("Kebab-ravintola")
    elif ensimmäinen_suunta == 3:
        print("Oma koti")
    elif ensimmäinen_suunta != 1 or 2 or 3:
        print("Tuolla numerolla ei löytynyt vaihtoehtoa.")


#aloita_peli()


# Tulostettavaa tekstiä hidastava funktio, jos haluaa pelin tuntuvan hitaammalta.
# 
# import sys
# import time
# 
# def type_text(text, delay=0.08):
#   for char in text:
#     sys.stdout.write(char)
#     sys.stdout.flush()
#     time.sleep(delay)
#   print()


# type_text("Tervetuloa pelaamaan peliä...")