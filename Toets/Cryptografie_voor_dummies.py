def versleutel_woord(woord, plaatsen):
    nieuwwoord = ''
    for i in range(len(woord)):
        if woord[i] == ' ':
            nieuwletter = '@'
        else:
            hoofdletter = woord[i].upper()
            positie = ord(hoofdletter)
            nieuwletter = chr(positie + int(plaatsen))
            if nieuwletter == '@':
                nieuwletter = ' '
        nieuwwoord += nieuwletter
    return nieuwwoord

def versleutel_zin(zin, plaatsen):
    nieuwzin = versleutel_woord(zin, plaatsen)
    return nieuwzin

def versleutel_woord(woord, n):

    versleuteld_woord = ''

    woord = woord.upper()

    for letter in woord:

        versleutelde_letter = chr(ord(letter) + n)

        if versleutelde_letter == '@':
            versleutelde_letter = ' '

        versleuteld_woord += versleutelde_letter

    return versleuteld_woord

def versleutel_zin(zin, getal):

    index_spatie = zin.find(' ')
    code = ''

    while index_spatie != -1:
        woord = zin[:index_spatie]
        zin = zin[index_spatie + 1:]

        code += '@' + versleutel_woord(zin, getal)
        index_spatie = zin.find(' ')

    if len(zin) > 0:
        code += '@' + versleutel_woord(zin, getal)

    return code