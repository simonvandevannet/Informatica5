def tel_woorden_dov(zin):
    return len(zin) - len(zin.replace(' ', '')) + 1



def tel_woorden(zin):

    aantal_spaties = 1

    for letter in zin:
        if letter == ' ':
            aantal_spaties += 1

    return aantal_spaties

print(tel_woorden('Ze weet al welke ze wil.'))