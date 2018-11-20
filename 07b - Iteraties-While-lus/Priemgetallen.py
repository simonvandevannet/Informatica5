getal = int(input('getal: '))
deler = 2
hulp = 0
while deler < getal:
    if getal % deler == 0:
        mes = '{} is geen priemgetal'.format(getal)
        hulp = 1
    deler += 1

if getal == 1:
    mes = '1 is geen priemgetal'
elif hulp == 0:
    mes = '{} is een priemgetal'.format(getal)

print(mes)