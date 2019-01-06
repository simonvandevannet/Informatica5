h = int(input('getal: '))
som = 0

for letter in str(h):
    som += int(letter)

if h % som == 0:
    mes = '{} is een Hashradgetal'.format(h)
else:
    mes = '{} is geen Hashradgetal'.format(h)

print(mes)