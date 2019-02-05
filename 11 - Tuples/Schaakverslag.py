def geldige_zet(zet):
    if len(zet) == 3:
        if zet[0] in 'KDTLP':
            if zet[1] in 'abcdefgh':
                if zet[2] in '12345678':
                    mes = True
                else:
                    mes = False
            else:
                mes = False
        else:
            mes = False
    elif len(zet) == 2:
        if zet[0] in 'abcdefgh':
            if zet[1] in '12345678':
                mes = True
            else:
                mes = False
        else: mes = False
    else:
        mes = False
    return mes

def geldige_zetten(zetten):
    zet = zetten[0]
    while geldige_zet(zet) == True:
        zetten = zetten[1:]
        if len(zetten) > 0:
            zet = zetten[0]
        else:
            zet = 'ABC'
    if len(zetten) == 0:
        mes = True
    else:
        mes = False
    return mes