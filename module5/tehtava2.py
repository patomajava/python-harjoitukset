luku = 0

while luku >= 0:
    luku = float(input("Anna luku senttimetreinä: "))
    if luku < 0:
        pass
    else:
        print(f"{luku} senttimetriä on {luku * 2.54} tuumaa.")