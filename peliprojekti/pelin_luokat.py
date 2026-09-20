class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.nälkätaso = 80
        self.raha = 5
        self.esineet = []

        
class Huone:
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