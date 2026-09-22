import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):

       self.rekisteritunnus = rekisteritunnus
       self.huippunopeus = huippunopeus
       self.nopeus = 0
       self.matka = 0


    def kiihdytä(self, muutos):

        if self.nopeus + muutos <= self.huippunopeus and self.nopeus + muutos > 0:
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
        return self.matka


autot = []

for i in range(1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    autot.append(auto)
 
while True: 
    for i in autot:
        auto = i.kiihdytä(random.randint(-10, 15))
        i.kulje(1)

    if i.matka >= 10000:
        break
    
print("")
print("Rekisterikilpi |   Huippunopeus  | Kuljettu matka")
print("--------------------------------------------------")

for auto in autot:
    print(f"{auto.rekisteritunnus:<14} | "
          f"{auto.huippunopeus:<10} km/h | "
          f"{auto.matka:<12} km")

print("--------------------------------------------------\n")