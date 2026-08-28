# suutari = input("Anna suutarin nimi: ")
# räätäli = input("Anna räätälin nimi: ")

# if suutari == räätäli:
#     print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")


# ikä = int(input("Anna ikä: "))
# paino = 0

# if 15 <= ikä < 18:
#     paino = float(input("Anna paino (kg): "))


# if ikä >= 15 and paino >= 55 or ikä >= 18:
#     print("Lääkkeen käyttö on sallittua.")


ikä = int(input("Anna ikäsi: "))

if ikä >= 65:
    print("Olet eläkeiässä.")

elif ikä >= 18:
    print("Olet työiässä.")

elif ikä >= 7:
    print("Olet koululainen.")

else:
    print("Olet pikkulapsi.")