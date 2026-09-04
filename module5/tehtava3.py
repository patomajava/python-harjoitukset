luku = (input("Anna luku: "))
suurin_luku = luku
pienin_luku = luku

while str(luku) != (""):

    if float(luku) > float(suurin_luku):
        suurin_luku = luku
    if float(luku) < float(pienin_luku):
        pienin_luku = luku
    else:
        print(luku)
        luku = ((input("Anna luku: ")))

if suurin_luku == "":
    print("Lukuja ei annettu, ohjelma sammuu.")
else:
    print(f"Suurin annettu luku oli {suurin_luku} ja pienin annettu luku oli {pienin_luku}. Ohjelma sammuu.")