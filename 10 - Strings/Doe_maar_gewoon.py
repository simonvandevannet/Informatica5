def doe_maar_gewoon(woord):
    for i in range(len(woord)):
        if woord[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and i + 1 <= len(woord) and woord[i+1] == woord[i].lower():
            woord = woord[:i] + woord[i].lower() + woord[i + 1:]
    return woord