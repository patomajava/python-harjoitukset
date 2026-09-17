kuukaudet = ("Tammiukuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")
järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
kuukausi = kuukaudet[järjestysnumero - 1]

if järjestysnumero == 12 or järjestysnumero == 1 or järjestysnumero == 2:
    print(f"{kuukausi}n vuodenaika on talvi.")
elif järjestysnumero == 3 or järjestysnumero == 4 or järjestysnumero == 5:
    print(f"{kuukausi}n vuodenaika on kevät.")
elif järjestysnumero == 6 or järjestysnumero == 7 or järjestysnumero == 8:
    print(f"{kuukausi}n vuodenaika on kesä.")
elif järjestysnumero == 9 or järjestysnumero == 10 or järjestysnumero == 11:
    print(f"{kuukausi}n vuodenaika on syksy.")