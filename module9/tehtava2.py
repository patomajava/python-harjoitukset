class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
       self.rekisteritunnus = rekisteritunnus
       self.huippunopeus = huippunopeus
       self.tämänhetkinen_nopeus = 0
       self.kuljettu_matka = 0


    def kiihdytä(self, nopeuden_muutos):
        if self.tämänhetkinen_nopeus + nopeuden_muutos <= self.huippunopeus and self.tämänhetkinen_nopeus + nopeuden_muutos > 0:
            self.tämänhetkinen_nopeus = self.tämänhetkinen_nopeus + nopeuden_muutos
            print(f"Auton nopeus on {self.tämänhetkinen_nopeus} km/h.")
        elif self.tämänhetkinen_nopeus + nopeuden_muutos > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
            print(f"Auton nopeus on {self.tämänhetkinen_nopeus} km/h.")
        elif self.tämänhetkinen_nopeus + nopeuden_muutos < 0:
            print("Auton nopeus on 0 km/h.")


auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
auto1.kiihdytä(-200)

#print(f"Auton rekisterikilpi: {auto1.rekisteritunnus}\nAuton huippunopeus: {auto1.huippunopeus}")
#print(f"Auton tämänhetkinen nopeus: {auto1.tämänhetkinen_nopeus}\nAuton kuljettu matka: {auto1.kuljettu_matka}")