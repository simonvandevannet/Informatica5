# invoer
a1 = int(input('Dobbelsteen 1 aanvaller: '))
a2 = int(input('Dobbelsteen 2 aanvaller: '))
a3 = int(input('Dobbelsteen 3 aanvaller: '))
v1 = int(input('Dobbelsteen 1 verdediger: '))
v2 = int(input('Dobbelsteen 2 verdediger: '))

# uitvoer
if a1 >= a2 >= a3 and v1 >= v2:
    if a1 > v1 and a2 > v2:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a1 <= v1 and a2 <= v2:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a1 >= a2 >= a3 and v2 >= v1:
    if a1 > v2 and a2 > v1:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a1 <= v2 and a2 <= v1:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a1 >= a3 >= a2 and v1 >= v2:
    if a1 > v1 and a3 > v2:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a1 <= v1 and a3 <= v2:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a1 >= a3 >= a2 and v2 >= v1:
    if a1 > v2 and a3 > v1:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a1 <= v1 and a2 <= v2:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a2 >= a1 >= a3 and v1 >= v2:
    if a2 > v1 and a1 > v2:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a2 <= v1 and a1 <= v2:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a2 >= a1 >= a3 and v2 >= v1:
    if a2 > v2 and a1 > v1:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a2 <= v2 and a1 <= v1:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a2 >= a3 >= a1 and v1 >= v2:
    if a2 > v1 and a3 > v2:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a2 <= v1 and a3 <= v2:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a2 >= a3 >= a1 and v2 >= v1:
    if a2 > v2 and a3 > v1:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a2 <= v2 and a3 <= v1:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a3 >= a1 >= a2 and v1 >= v2:
    if a3 > v1 and a1 > v2:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a3 <= v1 and a1 <= v2:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a3 >= a1 >= a2 and v2 >= v1:
    if a3 > v2 and a1 > v1:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a3 <= v2 and a1 <= v1:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a3 >= a2 >= a1 and v1 >= v2:
    if a3 > v1 and a2 > v2:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a3 <= v1 and a2 <= v2:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif a3 >= a2 >= a1 and v2 >= v1:
    if a3 > v2 and a2 > v1:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif a3 <= v2 and a2 <= v1:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')