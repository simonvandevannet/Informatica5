#input
speler_1 = input('Speler 1: ')
speler_2 = input('Speler 2: ')

#uitvoer
if speler_1 == 'blad':
    if speler_2 == 'blad':
        print('onbeslist')
    elif speler_2 == 'steen':
        print('speler 1 wint')
    else:
        print('speler 2 wint')
elif speler_1 == 'steen':
    if speler_2 == 'steen':
        print('onbeslist')
    elif speler_2 == 'blad':
        print('speler 2 wint')
    else:
        print('speler 1 wint')
elif speler_1 == 'schaar':
    if speler_2 == 'schaar':
        print('onbeslist')
    elif speler_2 == 'blad':
        print('speler 1 wint')
    else:
        print('speler 2 wint')