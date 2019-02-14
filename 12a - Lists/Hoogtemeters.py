def hoogtemeters(hoogtes):
    hoogtemeters = []
    for i in range(len(hoogtes) - 1):
        som = hoogtes[i + 1] - hoogtes[i]
        hoogtemeters.append(som)
    return hoogtemeters

def dalen_en_stijgen(hoogtes):
    som_dalen = 0
    som_stijgen = 0
    for i in range(len(hoogtes)):
        if hoogtes[i] > 0:
            som_stijgen += hoogtes[i]
        else:
            som_dalen += -hoogtes[i]
    return som_dalen, som_stijgen

print(hoogtemeters([22, 22]))
print(dalen_en_stijgen([-761, 286, -113, 649, -547]))