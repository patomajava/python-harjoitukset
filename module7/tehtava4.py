def lukujen_summa(luvut):
    luku = 0
    for i in luvut:
        luku += i
    return luku

lukulista = [1, 5, 8, 7, 10]

summa = lukujen_summa(lukulista)
print(f"Listan lukujen summa on: {summa}")