import math

pitsan_1_halkaisija = float(input("Anna pitsan 1 halkaisija (cm): "))
pitsan_1_hinta = float(input("Anna pitsan 1 hinta (€): "))
pitsan_2_halkaisija = float(input("Anna pitsan 2 halkaisija (cm): "))
pitsan_2_hinta = float(input("Anna pitsan 2 hinta (€): "))

def parempi_vastine(halkaisija1, hinta1, halkaisija2, hinta2):

    pitsa1_vastine = hinta1 / (math.pi * (halkaisija1 * 2))
    pitsa2_vastine = hinta2 / (math.pi * (halkaisija2 * 2))

    if pitsa1_vastine < pitsa2_vastine:
        return "Pitsan 1 vastine on parempi."
    elif pitsa2_vastine < pitsa1_vastine:
        return "Pitsan 2 vastine on parempi."
    else:
        return "Pitsan vastineet ovat samat!"

print(parempi_vastine(pitsan_1_halkaisija, pitsan_1_hinta, pitsan_2_halkaisija, pitsan_2_hinta))