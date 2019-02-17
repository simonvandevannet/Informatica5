def volgende_rij(lijst):
    volgende_rij = []
    for i in range(len(lijst) - 1):
        if lijst[i] == lijst[i+1]:
            volgende_rij.append(lijst[i])
        elif (lijst[i] == 'Y' and lijst[i + 1] == 'G') or (lijst[i] == 'G' and lijst[i + 1] == 'Y'):
            volgende_rij.append('R')
        elif (lijst[i] == 'R' and lijst[i + 1] == 'Y') or (lijst[i] == 'Y' and lijst[i + 1] == 'R'):
            volgende_rij.append('G')
        else:
            volgende_rij.append('Y')
    return volgende_rij

def driehoek(lijst):
    driehoek = [[], lijst]
    while len(driehoek[-1]) != 1:
        driehoek.append(volgende_rij(driehoek[-1]))
    driehoek.pop(0)
    return driehoek

def kleuren(lijst):
    somg = 0
    somr = 0
    somy = 0
    for i in range(len(lijst)):
        for j in range(len(lijst[i])):
            if lijst[i][j] == 'G':
                somg += 1
            elif lijst[i][j] == 'R':
                somr += 1
            else:
                somy += 1
    return somg, somr, somy



print(volgende_rij(['Y', 'R', 'G', 'Y', 'Y']))
print(driehoek(['G', 'G', 'G', 'G', 'G']))
print(kleuren([['Y', 'R', 'G', 'Y', 'Y'], ['G', 'Y', 'R', 'Y'], ['R', 'G', 'G'], ['Y', 'G'], ['R']]))