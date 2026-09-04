import random

arpakuutiot = int(input("Anna arpakuutioiden määrä: "))
arpakuutio = 0

for i in range(arpakuutiot):
    silmaluku = random.randint(1,6)
    arpakuutio = arpakuutio + 1
    print(f"Arpakuution {arpakuutio} silmaluku on: {silmaluku}")