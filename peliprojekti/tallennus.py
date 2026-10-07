import os

def tallenna_peli(pelaaja, kaikki_tilat):

    with open("tallennus.txt", "w", encoding="utf-8") as tiedosto:

        # PELAAJAN TIEDOT
        tiedosto.write(f"nimi={pelaaja.nimi}\n")
        tiedosto.write(f"ikä={pelaaja.ikä}\n")

        # PELAAJAN TILANNE
        tiedosto.write(f"\nsijainti={pelaaja.sijainti.nimi}\n")
        tiedosto.write(f"nälkä={pelaaja.nälkä}\n")
        tiedosto.write(f"raha={pelaaja.raha}\n")
        tiedosto.write(f"aika={pelaaja.aika}\n")

        # SALAISEN TUNNELLI AUKI VAI EI
        tiedosto.write(f"\nkoti_kerrat={pelaaja.koti_kerrat}\n")
        tiedosto.write(f"\nsalainen_kellari_avattu={pelaaja.salainen_kellari_avattu}\n")

        # PELAAJAN ESINEET
        esineet = []
        for esine in pelaaja.esineet:
            esineet.append(f"{esine.nimi}:{esine.arvo}")
        tiedosto.write(f"\npelaajan_esineet={'|'.join(esineet)}\n")


        # PELAAJAN TUOTTEET
        tuotteet = []
        for tuote in pelaaja.tuotteet:
            tuotteet.append(f"{tuote.nimi}:{tuote.hinta}:{tuote.ravintoarvo}")

        tiedosto.write(f"\npelaajan_tuotteet={'|'.join(tuotteet)}\n")

        # TILOJEN ESINEET

        for nimi, tila in kaikki_tilat.items():

            esineet = []
            
            for esine in tila.esineet:
                esineet.append(f"{esine.nimi}:{esine.arvo}")

            tiedosto.write(f"\ntila_{nimi}_esineet={'|'.join(esineet)}\n")


def lataa_peli():

    if not os.path.exists("tallennus.txt"):
        return None

    tiedot = {}

    with open("tallennus.txt", "r", encoding="utf-8") as tiedosto:

        for rivi in tiedosto:
            rivi = rivi.strip()

            if not rivi:
                continue

            avain, arvo = rivi.split("=", 1)
            tiedot[avain] = arvo

    return tiedot