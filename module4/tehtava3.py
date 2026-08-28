sukupuoli = str(input("Anna biologinen sukupuolesi (Mies/Nainen): "))
hemoglobiini = float(input("Anna hemoglobiiniarvosi: "))

if sukupuoli == "Mies" and hemoglobiini < 134:
    print("Sukupuolesi on mies, ja hemoglobiiniarvosi on alhainen.")

elif sukupuoli == "Mies" and hemoglobiini >= 134 and hemoglobiini <= 195:
    print("Sukupuolesi on mies, ja hemoglobiiniarvosi on normaali.")

elif sukupuoli == "Mies" and hemoglobiini > 195:
    print("Sukupuolesi on mies, ja hemoglobiiniarvosi on korkea")

elif sukupuoli == "Nainen" and hemoglobiini < 117:
    print("Sukupuolesi on nainen, ja hemoglobiiniarvosi on alhainen.")

elif sukupuoli == "Nainen" and hemoglobiini >= 117 and hemoglobiini <= 175:
    print("Sukupuolesi on nainen, ja hemoglobiiniarvosi on normaali.")

elif sukupuoli == "Nainen" and hemoglobiini > 175:
    print("Sukupuolesi on nainen ja hemoglobiiniarvosi on korkea.")

else:
    print("Virheellinen sukupuoli.")