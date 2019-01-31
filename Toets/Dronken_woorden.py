# Je hebt een BOB: de eerste letter van het woord drinkt niet en neem je gewoon over.
# De blaaskaak: alle letters op een even index groter dan 0 worden hoofdletters.
# Een volger: op een klinker (a, e, i, o of u) die in het nieuwe woord door regel 1 of 2 een hoofdletter geworden is, volgt altijd een hoofdletter.
# Ssst, een slappeling: alle andere letters vallen in slaap en worden of blijven kleine letters.



def dronken_worden(woord):
    nieuw_woord = woord[0]
    for i in range(1, len(woord)):

        # even letter?
        if i % 2 == 0:
            nieuw_woord += woord[i].upper()

        # oneven letter en vorige letter is hoofdletterklinker op einde nieuwe woord
        elif nieuw_woord[-1] in 'AEIOU':
            nieuw_woord += woord[i].upper()

        # oneven letter
        else:
            nieuw_woord += woord[i].lower()

    return nieuw_woord

print(dronken_worden('drinkeboer'))