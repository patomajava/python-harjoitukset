import random

luku = True

print ("Tämä ohjelma heittää noppaa, kunnes se tulostaa nopan suurimman mahdollisen numeron.")
suurin_silmaluku = int(input("Anna nopan maksimisilmäluku: "))

def nopan_numero(suurin_silmaluku):
    luku = random.randint(1, suurin_silmaluku)
    return luku

while luku != suurin_silmaluku:
    luku = nopan_numero(suurin_silmaluku)
    print(luku)

print("Vihdoinkin!")