# invoer
hoed1 = input('kleur hoed 1: ')
hoed2 = input('kleur hoed 2: ')
leugenaar = input('Wie zegt omgekeerde kleur? ')

# uitvoer
if leugenaar == '1':
    if hoed1 == 'wit' and hoed2 == 'wit':
        print('zwart')
        print('wit')
    elif hoed1 == 'zwart' and hoed2 == 'zwart':
        print('wit')
        print('zwart')
    elif hoed1 == 'wit' and hoed2 == 'zwart':
        print('wit')
        print('wit')
    else:
        print('zwart')
        print('zwart')
else:
    if hoed1 == 'wit' and hoed2 == 'wit':
        print('wit')
        print('zwart')
    elif hoed1 == 'zwart' and hoed2 == 'zwart':
        print('zwart')
        print('wit')
    elif hoed1 == 'wit' and hoed2 == 'zwart':
        print('zwart')
        print('zwart')
    else:
        print('wit')
        print('wit')