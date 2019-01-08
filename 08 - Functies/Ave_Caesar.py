def is_letter(n):
    if 64 < ord(n) < 91 or 96 < ord(n) < 123:
        mes = True
    else:
        mes = False
    return mes

def roteer_letter(n, x):
    letter = ord(n)
    if 64 < letter < 91:
        letter += x
        if letter > 90:
            letter -= 26
    elif 96 < letter < 123:
        letter += x
        if letter > 122:
            letter -= 26
    return chr(letter)

def versleutel(y, x):
    zin = ''
    for n in y:
        zin += roteer_letter(n, x)
    return zin