aantal = int(input('aantal basen: '))
woord = ''
letters = ''
aantal_verschillende = 0

for i in range(aantal):
    base = input('base: ')
    woord += base

for letter in woord:
    if letter not in letters:
        letters += letter + ' '
        aantal_verschillende += 1

if aantal_verschillende == 1:
    mes = 'soort base'
else:
    mes = 'verschillende soorten basen'

print('De DNA-keting bevat {} {}: {}'.format(aantal_verschillende, mes, letters))