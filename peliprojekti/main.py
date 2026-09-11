from pelin_funktiot import pelaajan_tiedot, päävalikko, aloita_peli, tulosta_tiedot, lempi_peli, muu_tieto


pelaajan_nimi, pelaajan_ikä = pelaajan_tiedot()
tietolista = [pelaajan_nimi, pelaajan_ikä, "", ""]


while True:
    try:
        pyydetty_toiminto = int(päävalikko())
    except ValueError:
        input("Annoit virheellisen numeron, yritä uudelleen. (Paina enteriä jatkaaksesi)")
        continue

    if pyydetty_toiminto == 0:
        print("\nOhjelma sulkeutuu.\n")
        exit()
    elif pyydetty_toiminto == 1:
        aloita_peli()
    elif pyydetty_toiminto == 2:
        tulosta_tiedot(tietolista)
    elif pyydetty_toiminto == 3:
        tietolista[2] = lempi_peli()
    elif pyydetty_toiminto == 4:
        tietolista[3] = muu_tieto()
    else:
        input("Tuolla numerolla ei löytynyt toimintoa. (Paina enteriä jatkaaksesi)")