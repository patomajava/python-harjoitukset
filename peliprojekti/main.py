from pelin_funktiot import pelaajan_tiedot
from pelin_funktiot import päävalikko
from pelin_funktiot import aloita_peli
from pelin_funktiot import tulosta_tiedot
from pelin_funktiot import lempi_peli


pelaajan_nimi, pelaajan_ikä = pelaajan_tiedot()
tietolista = [pelaajan_nimi, pelaajan_ikä]


while True:
    pyydetty_toiminto = int(päävalikko()) # Joskus herjaa erroria tuosta int:istä ihan sama minne pistää = ratkaise asia

    if pyydetty_toiminto == 0:
        print("\nOhjelma sulkeutuu.\n")
        exit()
    elif pyydetty_toiminto == 1:
        aloita_peli()
    elif pyydetty_toiminto == 2:
        tulosta_tiedot(tietolista)
    elif pyydetty_toiminto == 3:
        tietolista.insert(2, lempi_peli()) # Korjaa että vain 1 lempipeli voi olla olemassa kerrallaan. Ja yritä tulostaa lista niin että tiedon edessä näkyy, mikä tieto se on.