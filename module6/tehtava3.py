annettu_luku = int(input("Anna kokonaisluku: "))

if annettu_luku == 1:
    print("Luku 1 ei ole alkuluku.")
else:
    for luku in range(2, annettu_luku):
        if annettu_luku % luku == 0:
            print(f"{annettu_luku} ei ole alkuluku.")
            break
    else:
        print(f"{annettu_luku} on alkuluku.")