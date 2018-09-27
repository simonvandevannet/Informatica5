constante_van_avogrado = 6.020 * (10 ** 23)
molaire_massa_s = 32.06

#input
aantal_deeltjes_in_mol = float(input('Geef aantal deeltjes in mol: '))

#output
massa = aantal_deeltjes_in_mol * molaire_massa_s
aantal_deeltjes_s = aantal_deeltjes_in_mol * constante_van_avogrado

print(massa)
print(aantal_deeltjes_s)