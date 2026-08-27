leiviskat = float(input("Anna leiviskät: \n"))
naulat = float(input("Anna naulat: \n"))
luodit = float(input("Anna luodit: \n"))

luodit_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit

grammat = luodit_yhteensa * 13.3
kilogrammat = int(grammat // 1000)
jaannos_grammat = grammat % 1000

print("")
print("Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {jaannos_grammat} grammaa.")