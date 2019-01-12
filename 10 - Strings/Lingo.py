def hint(woord1, woord2):
    antwoord = ''
    for i in range(0, len(woord1)):
        if woord1[i] in woord2:
            if woord1[i] == woord2[i]:
                antwoord += woord1[i].upper()
            else:
                antwoord += woord1[i]
        else:
            antwoord += '.'
    return antwoord