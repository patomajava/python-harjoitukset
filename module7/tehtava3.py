def galloonat_litroiksi(galloona):
    litrat = galloona * 3.785
    return litrat

print("Tämä ohjelma muuntaa galloonat litroiksi, kunnes sille annetaan negatiivinen luku.")
galloona = True


while galloona >= 0:
    galloona = float(input("Anna galloonat: "))
    if galloona < 0:
        print("Ohjelma sammuu.")
        exit()
    litrat = galloonat_litroiksi(galloona)
    print(f"{galloona} galloonaa on {litrat} litraa.")