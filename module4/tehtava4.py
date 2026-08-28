print("Tämä ohjelma kertoo, onko antamasi vuosiluku karkausvuosi.")
vuosi = int(input("Anna vuosiluku: "))

if vuosi % 4 == 0 or vuosi % 400 == 0:
    print("Annettu vuosi on karkausvuosi")

else:
    print("Annettu vuosi ei ole karkausvuosi.")