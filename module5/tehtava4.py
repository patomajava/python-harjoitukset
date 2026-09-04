import random

luku = random.randint(1,10)
arvaus = int(input("Arvaa luku 1-10: "))

while arvaus != luku:
    if arvaus < luku:
        arvaus = int(input("Liian pieni arvaus, yritä uudelleen: "))
    elif arvaus > luku:
        arvaus = int(input("Liian suuri arvaus, yritä uudelleen: "))

print(f"Arvasit luvun oikein, luku oli {luku}.")