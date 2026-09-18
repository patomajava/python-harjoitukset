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
    
    def siirry_kerrokseen(self):
        while True:
            uusi_kerros = int(input("Siirry kerrokseen: "))

            if uusi_kerros == 0:
                break

            elif uusi_kerros > self.hissin_kerros and uusi_kerros <= self.korkein_kerros:
                while uusi_kerros != self.hissin_kerros:
                    self.hissin_kerros = self.kerros_ylös()
                print(f"Hissin lopullinen kerros on {self.hissin_kerros}.")

            elif uusi_kerros < self.hissin_kerros and uusi_kerros >= self.alin_kerros:
                while uusi_kerros != self.hissin_kerros:
                    self.hissin_kerros = self.kerros_alas()
                print(f"Hissin lopullinen kerros on {self.hissin_kerros}.")

hissi1 = Hissi(1, 8)

hissi1.siirry_kerrokseen()