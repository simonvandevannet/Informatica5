def kleur_toevoegen(lijst, kleur):
    if kleur == 'rood':
        lijst[0] += 1
    elif kleur == 'groen':
        lijst[1] += 1
    else:
        lijst[2] += 1
    return lijst

def is_wit(lijst):
    return lijst[0] == lijst[1] == lijst[2]

def verf_verzamelen(lijst):
    i = 1
    aantal_rood = 0
    aantal_groen = 0
    aantal_blauw = 0
    if lijst[0] == 'rood':
        aantal_rood += 1
    elif lijst[0] == 'groen':
        aantal_groen += 1
    else:
        aantal_blauw += 1
    while (aantal_rood != aantal_blauw or aantal_rood != aantal_groen) and i < len(lijst):
        if lijst[i] == 'rood':
            aantal_rood += 1
        elif lijst[i] == 'groen':
            aantal_groen += 1
        else:
            aantal_blauw += 1
        i += 1
    verdeling = [aantal_rood, aantal_groen, aantal_blauw]
    if i == len(lijst):
        mes = None
    else:
        mes = i, verdeling
    return mes


print(kleur_toevoegen([9, 2, 4], 'rood'))
print(is_wit([1, 3, 5]))
print(verf_verzamelen(['groen', 'groen', 'rood', 'groen', 'rood', 'groen', 'groen', 'rood', 'blauw', 'groen', 'groen', 'blauw', 'blauw', 'rood', 'rood', 'rood', 'blauw', 'rood']))
print(verf_verzamelen(['blauw', 'rood', 'groen', 'blauw', 'groen', 'rood', 'blauw', 'rood', 'blauw', 'rood', 'rood', 'blauw', 'blauw', 'rood', 'groen', 'rood', 'groen']))