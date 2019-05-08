# def woord_frequentie(zin):
#     dictionary = {}
#     zin = zin.split()
#     for i in range(len(zin)):
#         zin[i] = zin[i].lower()
#         if '.' in zin[i] or ',' in zin:
#             zin[i] = zin[i][0: -1]
#     for i in range(len(zin)):
#         if zin[i] in dictionary:
#             dictionary[zin[i]] += 1
#         else:
#             dictionary[zin[i]] = 1
#
#     return dictionary
#
# def woorden_per_frequentie(zin):
#     dictionary = {}
#     frequentie = woord_frequentie(zin)
#     for woord in frequentie:
#         if woord not in dictionary:
#             dictionary[frequentie[woord]] = [woord]
#         else:
#             dictionary[frequentie[woord]] = dictionary[frequentie[woord]].append(frequentie[woord])
#
#     return dictionary


def woord_frequentie(zin):
    frequentie = {}
    woorden = zin.split()
    for i in range(len(woorden)):
        woorden[i] = woorden[i].lower()
        if '.' in woorden[i] or ',' in woorden[i]:
            woorden[i] = woorden[i][0: -1]
    for woord in woorden:
        if woord in frequentie:
            frequentie[woord] += 1
        else:
            frequentie[woord] = 1
    return frequentie

def woorden_per_frequentie(zin):
    woorden_per_frequentie = {}
    frequentie = woord_frequentie(zin)
    for key, value in frequentie.items():
        if value in woorden_per_frequentie:
            woorden_per_frequentie[value] += [key]
        else:
            woorden_per_frequentie[value] = [key]
    return woorden_per_frequentie

def meest_gebruikte_woorden(zin):
    keymax = 0
    frequentie = woorden_per_frequentie(zin)
    for key, value in frequentie.items():
        if int(key) > keymax:
            keymax = int(key)
            maxwoorden = value
    return maxwoorden

print(woord_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))
print(woorden_per_frequentie('Dit is een zin. En nog een zin. En een laatste zin.'))
print(meest_gebruikte_woorden('Dit is een zin. En nog een zin. En een laatste zin.'))