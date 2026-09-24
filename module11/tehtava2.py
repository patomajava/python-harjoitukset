class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):

       self.rekisteritunnus = rekisteritunnus
       self.huippunopeus = huippunopeus
       self.nopeus = 0
       self.matka = 0


    def kiihdytä(self, muutos):

        if self.nopeus + muutos <= self.huippunopeus and self.nopeus + muutos >= 0:
            self.nopeus = self.nopeus + muutos

        elif self.nopeus + muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus

        elif self.nopeus + muutos < 0:
            self.nopeus = 0


    def kulje(self, tunnit):
        self.matka = self.matka + self.nopeus * tunnit


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Akkukapasiteetti: {self.akkukapasiteetti} kWh")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Tankin koko: {self.tankin_koko} litraa")


sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

print("- Sähköauto -")
sähköauto.tulosta_tiedot()

print("")

print("- Polttomoottoriauto -")
polttomoottoriauto.tulosta_tiedot()

sähköauto.nopeus = 180
polttomoottoriauto.nopeus = 165

print("")

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauto kulki: {sähköauto.matka} km")
print(f"Polttomoottoriauto kulki: {polttomoottoriauto.matka} km")