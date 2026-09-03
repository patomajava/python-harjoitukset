import random

luku = random.randint(1,10)
arvaus = int(input("Arvaa luku 1-10: "))

while arvaus != luku:
    arvaus = int(input("Arvauksesi oli väärin, yritä uudelleen: "))

print(f"Arvasit luvun oikein, se oli {luku}.")