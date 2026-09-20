from pelin_luokat import Pelaaja, Huone, Esine
from pelin_funktiot import ensimmäinen_valikko

# Luodaan ensimmäinen "Huone" nimeltä koti, pelaaja, sekä kodissa sijaitsevat esineet.
koti = Huone("Koti")
pelaaja = Pelaaja(nimi, koti)
palautuspullo_koti = Esine("Palautuspullo", 0.20)

# Näytetään pelaajalle pelin alun tarina, sekä tehdään ensimmäinen päätös pelaajan suunnasta.
ensimmäinen_valikko()