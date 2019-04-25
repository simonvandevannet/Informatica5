def verlaat_ploeg(naam, ploeg, dictionary):

    dictionary[ploeg].remove(naam)

    if dictionary[ploeg] == []:
        dictionary.pop(ploeg)

    return dictionary

def vervoegt_ploeg(naam, ploeg, dictionary):
    if ploeg in dictionary:
        dictionary[ploeg].append(naam)

    else:
        dictionary[ploeg] = [naam]

    return dictionary



print(verlaat_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
print(vervoegt_ploeg('Els','Sinbox',{'Sinbox': ['An', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
print(vervoegt_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))