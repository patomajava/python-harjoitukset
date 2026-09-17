lentoasemat = {}

while True:
    päätös = input("\nHaluatko syöttää uuden lentokentän tiedot vai hakea jo olemassa olevan lentokentän tiedot (uusi/vanha/lopeta): ")

    if päätös == "uusi":
        lentoasemat[input("Lentokentän ICAO koodi: ")] = input("Lentokentän nimi: ")

    elif päätös == "vanha":
        lentoasema = input("Anna haettavan lentokentän ICAO koodi: ")
        if lentoasema in lentoasemat:
            print(f"ICAO koodi {lentoasema} on {lentoasemat[lentoasema]}")

    elif päätös == "lopeta":
        break