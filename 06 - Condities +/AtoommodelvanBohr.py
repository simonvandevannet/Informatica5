# invoer
e = int(input('Geef aantal elektronen: '))

# berekening
if e == 1 or e == 2:
    resultaat = 'K'
elif 2 < e < 11:
    resultaat = 'L'
elif 10 < e < 29:
    resultaat = 'M'
elif 28 < e < 61:
    resultaat = 'N'
elif 60 < e < 93:
    resultaat = 'O'
elif 92 < e < 125:
    resultaat = 'P'
else:
    resultaat = 'Q'

# uitvoer
print('De ' + resultaat + '-schil is de buitenste schil van een stabiel atoom met ' + str(e) + ' elektronen.')