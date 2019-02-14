def nieuw_kaartspel(kleuren, waarden):

    kaartspel = []
    for kleur in kleuren:
        for waarde in waarden:
            kaart = kleur + waarde
            kaartspel.append(kaart)

    return kaartspel

def splits_kaartspel(kaartspel):

    deel1 = kaartspel[:(len(kaartspel))//2]
    deel2 = kaartspel[(len(kaartspel))//2:]

    return deel1, deel2

def faro_shuffle(deel1, deel2):
    shuffle = []
    for i in range(len(deel1)):
        shuffle.append(deel1[i])
        shuffle.append(deel2[i])

    if len(deel2) > len(deel1):
        shuffle.append(deel2[-1])

    return shuffle


print(nieuw_kaartspel(['blad ', 'steen ', 'schaar '],['1', '2', '3']))
print(splits_kaartspel(['dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1']))
print(faro_shuffle(['dood 0', 'dood 1', 'liefde 0'],['liefde 1', 'tijd 0', 'tijd 1']))