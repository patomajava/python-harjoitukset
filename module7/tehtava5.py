def karsi_luvut(luvut):
    karsitut_luvut = []

    for luku in luvut:
        if luku % 2 == 0:
            karsitut_luvut.append(luku)
    return karsitut_luvut

lukulista = [3, 2, 44, 5, 12, 13, 15, 20]

karsittu_lukulista = karsi_luvut(lukulista)

print(karsittu_lukulista)