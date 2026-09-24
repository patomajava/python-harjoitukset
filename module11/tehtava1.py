class Julkaisu():
    def __init__(self, nimi):
        self.julkaisun_nimi = nimi



class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(self.julkaisun_nimi)
        print(self.kirjoittaja)
        print(self.sivumäärä)



class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(self.julkaisun_nimi)
        print(self.päätoimittaja)


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_no_6 = Kirja("Hytti n:o 6", "Rosa Liksom", "200 sivua")

aku_ankka.tulosta_tiedot()
print("")
hytti_no_6.tulosta_tiedot()