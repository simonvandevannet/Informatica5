from math import sqrt

def binnen_of_buiten(m, c, p):
    straal = sqrt(pow((m[0] - c[0]), 2) + pow((m[1] - c[1]),2))
    afstand = sqrt(pow((m[0] - p[0]), 2) + pow((m[1] - p[1]), 2))

    if straal == afstand:
        mes = 'op'
    elif straal > afstand:
        mes = 'binnen'
    else:
        mes = 'buiten'

    return mes, round(afstand, 4)

print(binnen_of_buiten((7, -1),(-9, -32),(12, -48)))