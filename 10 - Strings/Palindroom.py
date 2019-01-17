def is_palindroom(woord):
    nieuwwoord = ''
    for i in range(0, len(woord)):
        nieuwwoord += woord[-1 -i]
    if woord == nieuwwoord:
        mes = True
    else:
        mes = False
    return mes

def palindroom(woord):

    i = 0

    while woord[i]  == woord[-i - 1] and i < len(woord) // 2:
        i += 1

    return i == len(woord) // 2

print(palindroom('lepel'))

