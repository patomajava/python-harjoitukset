import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):

       self.rekisteritunnus = rekisteritunnus
       self.huippunopeus = huippunopeus
       self.nopeus = 0
       self.matka = 0


    def kiihdytä(self, muutos):

        if self.nopeus + muutos <= self.huippunopeus and self.nopeus + muutos >= 0:
            self.nopeus = self.nopeus + muutos
            #print(f"Auton nopeus on {self.nopeus} km/h.")

        elif self.nopeus + muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus
            #print(f"Auton nopeus on {self.nopeus} km/h.")

        elif self.nopeus + muutos < 0:
            self.nopeus = 0
            #print(f"Auton nopeus on {self.nopeus} km/h.")


    def kulje(self, tunnit):
        self.matka = self.matka + self.nopeus * tunnit
        #print(f"Kuljettu matka on {self.matka} kilometriä.")


class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, autolista):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("")
        print("Rekisterikilpi | Huippunopeus | Kuljettu matka")
        print("------------------------------------------------")

        for auto in self.autolista:
            print(f"{auto.rekisteritunnus:<14} | "
                  f"{auto.huippunopeus:<10} km/h | "
                  f"{auto.matka:<12} km")

        print("------------------------------------------------\n")

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.matka >= self.kilpailun_pituus:
                return True

        return False

autolista = []

for i in range(1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    autolista.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autolista)

tunti = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

print("Kilpailu on ohi!")
kilpailu.tulosta_tilanne()