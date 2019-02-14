def ik_heb_gemoord(lijst, ik):

    if len(lijst) != 1:
        for i in range(len(lijst)):
            if lijst[i - 1] == ik:
                lijst = lijst[: i] + lijst[i + 1:]

    for i in range(len(lijst)):

        if lijst[i] == ik and lijst[i] == lijst[-1]:
            opdracht = lijst[0]

        elif lijst[i] == ik:
            opdracht = lijst[i + 1]

    return opdracht, lijst


def ik_ben_vermoord(lijst, dode):

    for i in range(len(lijst)):

        if lijst[i] == dode and lijst[i] == lijst[-1]:
            opdracht = lijst[0]

        elif lijst[i] == dode:
            opdracht = lijst[i + 1]

    if len(lijst) != 1:
        for i in range(len(lijst)):
            if lijst[i] == dode:
                lijst = lijst[:i] + lijst[i + 1:]

    return opdracht, lijst

print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'joris'))
print(ik_ben_vermoord(['jan', 'piet', 'joris'],'joris'))


#########################################################################################################


def ik_heb_gemoord(lijst, moordenaar):
    # slachtoffer schrappen
    index_moordenaar = lijst.index(moordenaar)
    index_slachtoffer = (index_moordenaar + 1) % len(lijst)

    lijst[index_slachtoffer: index_slachtoffer + 1] = []

    # nieuw doel aan moordenaar geven
    index_moordenaar = lijst.index(moordenaar)
    index_nieuw_doel = (index_moordenaar + 1) % len(lijst)

    return lijst, lijst[index_nieuw_doel]