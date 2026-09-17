class Pelaaja:
    def __init__(self, nimi):
        self.nimi = nimi
        self.elämät = 3
        self.kolikot = 0
        self.pisteet = 0

pelaaja = Pelaaja("Mario")

#print(f"Pelaajan nimi on {pelaaja.nimi}, ja hänellä on {pelaaja.elämät} elämää.")

print("--Pelaajan tiedot--")
print(f"   Nimi: {pelaaja.nimi}\n   Elämät: {pelaaja.elämät}")
print(f"   Kolikot: {pelaaja.kolikot}\n   Pisteet: {pelaaja.pisteet}")