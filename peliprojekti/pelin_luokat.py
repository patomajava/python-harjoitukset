class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti

        self.nälkä = 20
        self.raha = 0.40
        self.aika = 480

        self.esineet = []
        self.tuotteet = []


    def liiku_seuraavaan_paikkaan(self, uusi_tila):

        self.sijainti = uusi_tila

    def ota_esine(self, esine):

        self.esineet.append(esine)

    def osta_tuote(self, tuote):

        self.raha -= tuote.hinta
        self.tuotteet.append(tuote)

    def syö(self, tuote):
        self.tuotteet.remove(tuote)

        self.nälkä -= tuote.ravintoarvo

    def ajankulu(self, aika):

        self.aika += aika

        self.nälkä += aika // 30

    def aika(self):

        print(f"Kello on {self.aika // 60}:{self.aika % 60}.")


# Tila on pelimaailmasta löytyvä paikka tai alue, jossa pelaaja voi olla, ja tehdä asioita
class Tila:
    def __init__(self, nimi):
        self.nimi = nimi
        self.esineet = []
        self.tuotteet = []
        self.yhteydet = {}

    def lisää_esine(self, esine):

        self.esineet.append(esine)

    def lisää_tuote(self, tuote):

        self.tuotteet.append(tuote)

    def lisää_yhteys(self, nimi, tila):

        self.yhteydet[nimi] = tila


# Esineet ovat pelimaailmasta löytyviä asioita, jotka eivät ole tuotteita. Näitä esineitä voi myydä.
class Esine:
    def __init__(self, nimi, arvo):
        self.nimi = nimi
        self.arvo = arvo


# Tuotteet ovat kaupoissa tai ravintoloissa esiintyviä esineitä ja niillä on hinta. Näitä esineitä ei voi myydä.
class Tuote:
    def __init__(self, nimi, hinta, ravintoarvo):
        self.nimi = nimi
        self.hinta = hinta
        self.ravintoarvo = ravintoarvo