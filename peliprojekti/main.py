from päävalikko import pelaajan_tiedot, päävalikko
from peli import aloita_peli

pelaajan_nimi, pelaajan_ikä = pelaajan_tiedot()

while True:
    pelaaja = päävalikko(pelaajan_nimi, pelaajan_ikä)
    aloita_peli(pelaaja)