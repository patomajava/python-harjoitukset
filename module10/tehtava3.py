class Hissi():
    def __init__(self, alin_kerros, korkein_kerros):
        self.korkein_kerros = korkein_kerros
        self.alin_kerros = alin_kerros
        self.hissin_kerros = 0

    def kerros_ylös(self):
        self.hissin_kerros += 1
        print(f"Hissi on kerroksessa {self.hissin_kerros}.")
        return self.hissin_kerros
 
    def kerros_alas(self):
        self.hissin_kerros -= 1
        print(f"Hissi on kerroksessa {self.hissin_kerros}.")
        return self.hissin_kerros  
    
    def siirry_kerrokseen(self, uusi_kerros):

            if uusi_kerros > self.hissin_kerros and uusi_kerros <= self.korkein_kerros:
                while uusi_kerros != self.hissin_kerros:
                    self.hissin_kerros = self.kerros_ylös()
                print(f"Hissin lopullinen kerros on {self.hissin_kerros}.")

            elif uusi_kerros < self.hissin_kerros and uusi_kerros >= self.alin_kerros:
                while uusi_kerros != self.hissin_kerros:
                    self.hissin_kerros = self.kerros_alas()
                print(f"Hissin lopullinen kerros on {self.hissin_kerros}.")


class Talo:
    def __init__(self, alin_kerros, korkein_kerros, hissien_määrä):
        self.korkein_kerros = korkein_kerros
        self.alin_kerros = alin_kerros
        self.hissien_määrä = hissien_määrä

        self.hissit = []

        for i in range(self.hissien_määrä):
            self.hissit.append(Hissi(alin_kerros, korkein_kerros))

    def aja_hissiä(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero]
        hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(0)
            print("Hissi on kerroksessa 0.")


talo = Talo(1, 8, 4)

talo.aja_hissiä(1, 4)
talo.aja_hissiä(3, 7)
talo.palohälytys()