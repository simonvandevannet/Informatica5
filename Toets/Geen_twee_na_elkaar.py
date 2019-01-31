def ontdubbelen(woord):
    beginwoord = woord
    for i in range(len(woord)):
        if i + 1 <= len(woord) and woord[i] == woord[i + 1]:
            woord = woord
        elif i + 2 <= len(woord) and woord[i] == woord[i + 1] == woord[i + 2]:
            woord = woord
        else:
            woord += woord[i]
    woord = woord[len(beginwoord):]
    return woord

def ontdubbel(woord):

    nieuw_woord = woord[0]

    for i in range(1, len(woord)):

        if woord[i] != woord[i - 1]:
            nieuw_woord += woord[i - 1]

    return nieuw_woord