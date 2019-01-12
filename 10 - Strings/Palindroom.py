def is_palindroom(woord):
    nieuwwoord = ''
    for i in range(0, len(woord)):
        nieuwwoord += woord[-1 -i]
    if woord == nieuwwoord:
        mes = True
    else:
        mes = False
    return mes