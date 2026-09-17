class Hero:
    sankarien_määrä = 0

    def __init__(self, nimi, tyyppi, kyky, aseen_aani, huudahdus="Hello!"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.kyky = kyky
        self.huudahdus = huudahdus
        self.aseen_aani = aseen_aani
        Hero.sankarien_määrä += 1


    def voice_line(self, kerrat):
        for i in range(kerrat):
            print(f"{self.huudahdus}")


    def shooting(self):
        print(self.aseen_aani)


hero1 = Hero("Tracer", "Damage", "Recall", "brrrr", "You got it!")
hero2 = Hero("Wrecking Ball", "Tank", "Piledriver", "KLONK!")


#print(f"{hero1.nimi} kuuluu rooliin '{hero1.tyyppi}'. Sankarin kyky on {hero1.kyky}, ja sen Voice Line on '{hero1.huudahdus}'")
#print(f"{hero2.nimi} kuuluu rooliin '{hero2.tyyppi}'. Sankarin kyky on {hero2.kyky}, ja sen Voice Line on '{hero2.huudahdus}'")

#hero1.voice_line(1)
#hero2.voice_line(2)

hero1.shooting()
hero2.shooting()

print(f"Sankarien määrä yhteensä: {Hero.sankarien_määrä}")