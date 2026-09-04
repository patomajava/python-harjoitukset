luvut = []

luku = input("Anna luku: ")

while luku != "":
    luvut.append(float(luku))
    luku = input("Anna seuraava luku: ")

luvut.sort(reverse=True)

print("Viisi suurinta lukua pienimpään ovat: ")

for luku in luvut[:5]:
    print(luku)