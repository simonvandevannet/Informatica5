hendel_trekken =  input('Trek aan de hendel van de wissel? (ja/nee): ')
man_duwen = input('Man van de brug duwen? (ja/nee): ')

if hendel_trekken == 'ja' and man_duwen == 'ja':
    print('2')

elif hendel_trekken == 'ja':
    print('1')

elif hendel_trekken == 'nee' and man_duwen == 'ja':
    print('1')

else:
    print('5')