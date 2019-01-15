def positie_laagste_ascii(woord):
    positie = 0
    laagste = ord(woord[0])
    for i in range(1, len(woord)):
        if ord(woord[i]) < laagste:
            laagste = ord(woord[i])
            positie = i
    return positie

def sorteer(woord):
    nieuwwoord = ''
    while len(woord) > 0:
        nieuwwoord += woord[positie_laagste_ascii(woord)]
        woord = woord[:positie_laagste_ascii(woord)] + woord[positie_laagste_ascii(woord) + 1 :]
    return nieuwwoord

def is_alfabetisch(woord):
    if woord == sorteer(woord):
        mes = True
    else:
        mes = False
    return mes