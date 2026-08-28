kuhan_pituus = int(input("Anna kuhan pituus senttimetreinä: "))

if kuhan_pituus < 37:
    print(f"Kuhasi on alimittainen {37-kuhan_pituus} sentillä. Päästä kuha takaisin kasvamaan.")

else:
    print("Kuhasi on tarpeeksi iso!")