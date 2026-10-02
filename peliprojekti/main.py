from päävalikko import pelaajan_tiedot, päävalikko
from peli import aloita_peli

with open("intro.txt", "r", encoding="utf-8") as tiedosto:
    print(tiedosto.read())

input("\n[Enter] Käynnistä peli")
print("\033[H\033[J", end="")

pelaajan_nimi, pelaajan_ikä = pelaajan_tiedot()

while True:

    päävalikko(pelaajan_nimi, pelaajan_ikä)
    aloita_peli(pelaajan_nimi)