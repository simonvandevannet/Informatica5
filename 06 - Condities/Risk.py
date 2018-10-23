# invoer
a1 = int(input('Dobbelsteen 1 aanvaller: '))
a2 = int(input('Dobbelsteen 2 aanvaller: '))
a3 = int(input('Dobbelsteen 3 aanvaller: '))
v1 = int(input('Dobbelsteen 1 verdediger: '))
v2 = int(input('Dobbelsteen 2 verdediger: '))

# uitvoer
middelste_getal = a1 + a2 + a3 - max(a1, a2, a3) - min(a1, a2, a3)

if max(a1, a2, a3) > max(v1, v2):
    if middelste_getal > min(v1, v2):
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
else:
    if middelste_getal > min(v1, v2):
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
    else:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')