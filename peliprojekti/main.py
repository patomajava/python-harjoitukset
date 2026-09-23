from päävalikko import pelaajan_tiedot, päävalikko
from peli import aloita_peli


# Kysytään pelaajan nimi ja ikä, jotta tiedetään että pelaaja on tarpeeksi vanha pelaamaan peliä.
pelaajan_nimi, pelaajan_ikä = pelaajan_tiedot()

while True:

# Ajetaan ohjelman päävalikko. Päävalikko palautuu tänne vain jos pelaaja valitsee komennon "aloita peli". Silloin ohjelma ajaa aloita peli Funktion, joka sitten luo pelimaailman ja pelivalikon.
    päävalikko(pelaajan_nimi, pelaajan_ikä)
    aloita_peli(pelaajan_nimi)