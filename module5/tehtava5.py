kayttaja = "python"
salasana = "rules"

kayttaja_arvaus = str(input("Anna käyttäjätunnus: "))
salasana_arvaus = str(input("Anna salasana: "))
arvauskerrat = 1

while kayttaja_arvaus != kayttaja and salasana_arvaus != salasana:
    if arvauskerrat >= 5:
        break

    print("Pääsy evätty.")

    kayttaja_arvaus = str(input("\nAnna käyttäjätunnus: "))
    salasana_arvaus = str(input("Anna salasana: "))
    arvauskerrat = arvauskerrat + 1

if kayttaja_arvaus == kayttaja and salasana_arvaus == salasana:
    print("Tervetuloa!")

elif arvauskerrat >= 5:
    print("Pääsy evätty, liian monta yritystä.")