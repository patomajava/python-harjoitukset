class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        # self.nälkätaso = 80
        self.raha = 0.40
        self.esineet = []

    def liiku_seuraavaan_paikkaan(self, nykyinen_huone, uusi_huone):
        print(f"Siirryt paikasta {nykyinen_huone} paikkaan {uusi_huone}.")

    def keraa_esine(self, esine):
        print(f"Olet kerännyt esineen {esine}.")

    def osta_tuote(self, tuote):
        print(f"Olet ostanut tuotteen {tuote}.")


# Tila on pelimaailmasta löytyvä paikka tai alue, jossa pelaaja voi olla, ja tehdä asioita
class Tila:
    def __init__(self, nimi):
        self.nimi = nimi
        self.esineet = []
        self.tuotteet = []


# Esineet ovat pelimaailmasta löytyviä asioita, jotka eivät ole tuotteita. Näitä esineitä voi myydä.
class Esine:
    def __init__(self, nimi, arvo):
        self.nimi = nimi
        self.arvo = arvo


# Tuotteet ovat kaupoissa tai ravintoloissa esiintyviä esineitä ja niillä on hinta. Näitä esineitä ei voi myydä.
class Tuote:
    def __init__(self, nimi, hinta):
        self.nimi = nimi
        self.hinta = hinta