import random

luku = True

def nopan_numero():
    luku = random.randint(1, 6)
    return luku

print("Tämä ohjelma tulostaa nopan heittoja kunnes silmäluku on 6.")

while luku != 6:
    luku = nopan_numero()
    print(luku)

print("Vihdoinkin!")