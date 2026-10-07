class Pelaaja:
    def __init__(self, nimi, ikä, sijainti):
        self.nimi = nimi
        self.ikä = ikä
        self.sijainti = sijainti
        self.salainen_kellari = None

        self.nälkä = 10
        self.raha = 0.0
        self.aika = 480

        self.esineet = []
        self.tuotteet = []

        self.koti_kerrat = 0
        self.salainen_kellari_avattu = False

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

        if self.nälkä < 0:
            self.nälkä = 0

    def ajankulu(self, aika):
        self.aika += aika
        self.nälkä += aika * 14 / 60
        if self.nälkä > 100:
            self.nälkä = 100

    def kello(self):
        print(f"Kello: {self.aika // 60:02d}:{self.aika % 60:02d}")


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

class Esine:
    def __init__(self, nimi, arvo):
        self.nimi = nimi
        self.arvo = arvo

class Tuote:
    def __init__(self, nimi, hinta, ravintoarvo):
        self.nimi = nimi
        self.hinta = hinta
        self.ravintoarvo = ravintoarvo