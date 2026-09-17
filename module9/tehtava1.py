class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
       self.rekisteritunnus = rekisteritunnus
       self.huippunopeus = huippunopeus
       self.tämänhetkinen_nopeus = 0
       self.kuljettu_matka = 0

auto1 = Auto("ABC-123", "142 km/h")

print(f"Auton rekisterikilpi: {auto1.rekisteritunnus}\nAuton huippunopeus: {auto1.huippunopeus}")
print(f"Auton tämänhetkinen nopeus: {auto1.tämänhetkinen_nopeus}\nAuton kuljettu matka: {auto1.kuljettu_matka}")