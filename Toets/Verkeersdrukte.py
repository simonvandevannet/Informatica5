# invoer
dv = float(input('verkeersdichtheid vrachtvervoer: '))
vv = float(input('snelheid vrachtvervoer: '))
da = float(input('verkeersdichtheid personenvervoer: '))
va = float(input('snelheid personenvervoer: '))

# berekening pv en pa
pv = min((vv * dv / 40), 1)
pa = min((va * da / 40), 1)

# berekening kleurcode
if min(pv, pa) > 0.7:
    mes = 'zwart'
elif max(pv, pa) > 0.7 and max(pv, pa) - min(pv, pa) < 0.2:
    mes = 'rood'
elif max(pv, pa) - min(pv, pa) > 0.7:
    mes = 'geel'
else:
    mes = 'groen'

# uitvoer
print(mes)