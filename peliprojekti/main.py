import os
from päävalikko import pelaajan_tiedot, päävalikko
from peli import aloita_peli

# MUUTETAAN HAKEMISTO JOTTA TIEDOSTOT TOIMIVAT OIKEIN.
os.chdir(os.path.dirname(__file__))

# AVATAAN JA LUETAAN PELIN ALOITUSTEKSTI.
with open("intro.txt", "r", encoding="utf-8") as tiedosto:
    input(tiedosto.read() + "\n\nPaina [Enter] aloittaaksesi pelin")

# TÄLLÄ LAUSEELLA TYHJENNETÄÄN TERMINAALI.
print("\033[H\033[J", end="")

pelaajan_nimi, pelaajan_ikä = pelaajan_tiedot()

tietolista = [pelaajan_nimi, pelaajan_ikä, "", ""]

# AJETAAN PÄÄVALIKON JA PELIVALIKON LOPUTON SILMUKKA.
while True:
    päävalikko(tietolista)
    aloita_peli(pelaajan_nimi)