def bereken_prijs(zin):
    lengte = zin.find('<')
    einde = zin.find('>')
    bedrag = float(zin[lengte + 1 : einde])
    totaal = lengte * bedrag
    nieuwzin = zin[:lengte]
    return nieuwzin, totaal

def toon_boodschappen(zinnen):
    totaal = 0
    boodschappen = ''
    while len(zinnen) > 0:
        lengte = zinnen.find('<')
        einde = zinnen.find('>')
        bedrag = float(zinnen[lengte + 1 : einde])
        totaal += lengte * bedrag
        boodschappen += zinnen[:lengte]
        zinnen = zinnen[einde + 1:]
        if len(zinnen) > 0:
            boodschappen += '\n'
    uitv = str(totaal) + '\n' + boodschappen
    return uitv