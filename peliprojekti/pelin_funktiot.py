def aloita_peli():
    #input("\nPeli on vielä kesken :)\n\nPaina enteriä jatkaaksesi")
    print("\n\nTervetuloa pelaamaan peliä!\n\n")

    print("Olet juuri herännyt, kello on 8.15 ja sinulla on kova nälkä. Lähdet etsimään ruokaa keittiösi kaapeista... mutta mitään ei löydy. Kaapit ovat tyhjentyneet yön aikana täysin, ja sinun nälkäsi vain kasvaa.\n")

    print("Sinun täytyy nyt lähteä etsimään ruokaa, mutta mistä?\n")

    ensimmäinen_suunta = 0

    try:
        ensimmäinen_suunta = int(input("1. Lähdet ruokakauppaan, johon on pitkä matka, mutta siellä hinnat ovat halpoja...\n2. Lähdet lähimpään Kebab-ravintolaan, se ei ole yhtä kaukana kuin ruokakauppa, mutta siellä hinnat ovat kalliimpia...\n3. Mietit, pitäisikö sinun murtautua naapuriin, sillä hänellä taatusti olisi ruokaa. Tiedät naapurin olevan erittäin tarkka, ja tiedät ettei hän poistu kotoaan usein. Mutta sinulla on nälkä, ja naapuri on lähin vaihtoehtosi...\n\nMinkä vaihtoehdon valitset: "))
    except ValueError:
        print("Virheellinen valinta, palataan päävalikkoon.")

    if ensimmäinen_suunta == 1:
        print("Ruokakauppa")
    elif ensimmäinen_suunta == 2:
        print("Kebab-ravintola")
    elif ensimmäinen_suunta == 3:
        print("Naapuri")
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