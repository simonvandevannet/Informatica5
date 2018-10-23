# invoer
temperatuur = float(input('Geef temperatuur: '))
lichtkracht = float(input('Geef lichtkracht: '))

# berekening
if lichtkracht > 10000:
    print('superreuzen (a)')
elif 1000 < lichtkracht < 10000:
    print('superreuzen (b)')
elif 100 < lichtkracht < 1000:
    if temperatuur > 7500:
        print('hoofdreeks')
    else:
        print('heldere reuzen')
elif 10 < lichtkracht < 100:
    if temperatuur > 6000:
        print('hoofdreeks')
    else:
        print('reuzen')
elif 0.01 < lichtkracht < 10:
    print('hoofdreeks')
elif 0.0001 < lichtkracht < 0.01:
    if temperatuur > 5000:
        print('witte dwergen')
    else:
        print('hoofdreeks')
else:
    if temperatuur > 3000:
        print('witte dwergen')
    else:
        print('hoofdreeks')