kaart = int(input('kaart: '))
totaal = 0

while kaart != 0:
    totaal += kaart
    if totaal < 21:
        kaart = int(input('kaart: '))
    else:
        kaart = 0

if totaal == 21:
    mes = 'Gewonnen!'
elif totaal > 21:
    mes = 'Verbrand ({})'.format(totaal)
else:
    mes = 'Voorzichtig gespeeld ({})'.format(totaal)

print(mes)