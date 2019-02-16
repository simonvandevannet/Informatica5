def printbaar_rek(lijst):
    rek = ''.join(lijst[0])
    for i in range(1, len(lijst)):
        rek = ''.join(lijst[i]) + '\n' + rek
    return rek


def speel(kleur, plaats, lijst):
    i = 0
    while lijst[i][plaats] != 'O':
        i += 1
    lijst[i][plaats] = kleur
    return lijst


print(printbaar_rek([['R', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))
print(speel('G',3,[['R', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))