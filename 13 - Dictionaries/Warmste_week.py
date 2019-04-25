def gift_inschrijven(gift, lijst):

    if gift[0] in lijst:
        lijst[gift[0]] += gift[1]
    else:
        lijst[gift[0]] = gift[1]

    return lijst

print(gift_inschrijven(('5IN', 73.81),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 232.48}))