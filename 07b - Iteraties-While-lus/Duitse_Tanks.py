serienummer = int(input('serienummer: '))
max = 0
aantal = 0

while serienummer >= 0:
    if serienummer > max:
        max = serienummer
    aantal += 1
    serienummer = int(input('serienummer: '))

t = (((aantal + 1) * max) / aantal) - 1

print('Het aantal geproduceerde tanks wordt geschat op {}.'.format(round(t)))