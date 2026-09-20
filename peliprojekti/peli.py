from pelin_luokat import Pelaaja, Huone, Esine
from pelin_funktiot import ensimmäinen_valikko


def aloita_peli(pelaaja):
    # Luodaan ensimmäinen "Huone" nimeltä koti, pelaaja, sekä kodissa sijaitsevat esineet.
    koti = Huone("Koti")
    pelaaja1 = Pelaaja(pelaaja, koti)
    palautuspullo_koti = Esine("Palautuspullo", 0.20)

    # Näytetään pelaajalle pelin alun tarina, sekä tehdään ensimmäinen päätös pelaajan suunnasta.
    ensimmäinen_valikko()