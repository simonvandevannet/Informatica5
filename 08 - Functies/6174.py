def splits(n):
    g1 = int(n) // 1000
    g2 = int(n) // 100 - 10 * g1
    g3 = int(n) // 10 - 100 * g1 - 10 * g2
    g4 = int(n) - 1000 * g1 - 100 * g2 - 10 * g3
    return g1, g2, g3, g4

def oplopende_cijfers(g1, g2, g3, g4):
    g = g1, g2, g3, g4
    oplopend = sorted(g)
    return tuple(oplopend)

def op_af_getallen(g1, g2, g3, g4):
    op = str(g1) + str(g2) + str(g3) + str(g4)
    af = str(g4) + str(g3) + str(g2) + str(g1)
    return op, af

def verschil(op, af):
    verschil = int(op) - int(af)
    return str(verschil)

def kaprekar(n):
    g1, g2, g3, g4 = splits(n)
    op, af = op_af_getallen(g1, g2, g3, g4)
    verschil = verschil(op, af)
    bewerking = '{} - {} = {}'.format(op, af, verschil)
    while verschil != 6174:
        bewerking += '{} - {} = {}'.format(op, af, verschil)
    return bewerking