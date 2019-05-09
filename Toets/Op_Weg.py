def bestaat_weg(stad1, stad2, kaart):
    return stad2 in kaart[stad1]


def geen_dubbelburen(stad1, stad2, kaart):

    buren1 = set(kaart[stad1])
    buren2 = set(kaart[stad2])
    geen_dubbelburen = buren2.difference(buren1)
    geen_dubbelburen.update(buren1.difference(buren2))
    geen_dubbelburen.discard(stad1)
    geen_dubbelburen.discard(stad2)

    return geen_dubbelburen


def bereikbaarheid_meest_afgelegen_stad(kaart):

    minlengte = 10
    for value in kaart.values():
        if len(value) < minlengte:
            minlengte = len(value)

    return minlengte

def bestaat_route(route, kaart):

    i = 0
    mes = True
    while i <= len(route) - 2 and mes == True:
        if route[i + 1] in kaart[route[i]]:
            mes = True
            i += 1
        else:
            mes = False

    return mes


kaart = {'Brugge': {'Gent', 'Antwerpen'}, 'Kortrijk': {'Gent'}, 'Gent': {'Antwerpen', 'Kortrijk', 'Brugge'}, 'Antwerpen': {'Gent', 'Brussel', 'Brugge'}, 'Brussel': {'Hasselt', 'Antwerpen'}, 'Hasselt': {'Brussel'}}


print(bestaat_weg('Brussel', 'Hasselt', kaart))
print(geen_dubbelburen('Kortrijk', 'Antwerpen', kaart))
print(bereikbaarheid_meest_afgelegen_stad(kaart))
print(bestaat_route(['Hasselt', 'Brussel', 'Antwerpen', 'Brugge', 'Gent', 'Kortrijk'], kaart))