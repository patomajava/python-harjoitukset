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
            self.tämänhetkinen_nopeus = 0
            print(f"Auton nopeus on {self.tämänhetkinen_nopeus} km/h.")


    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + self.tämänhetkinen_nopeus * tunnit
        print(f"Kuljettu matka on {self.kuljettu_matka} kilometriä.")



auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
#auto1.kiihdytä(-200)

auto1.kulje(1.5)