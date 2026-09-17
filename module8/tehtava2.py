nimet = set()

while True:
    nimi = input("\nAnna nimi: ")

    if nimi == "":
        break

    if nimi in nimet:
        print(f"{nimi} on aiemmin syötetty nimi.")
        
    else:
        nimet.add(nimi)
        print(f"{nimi} on uusi nimi.")