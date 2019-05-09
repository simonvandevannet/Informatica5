def vergeten_woorden(tekst, verplicht):
    woorden = set(tekst.split())

    # verplichte woorden
    aantal_verplicht = len(verplicht)

    # vergeten woorden
    aantal_vergeten = len(verplicht.difference(woorden))

    # gebruikte woorden
    aantal_gebruikte = len(verplicht.intersection(woorden))


    return aantal_verplicht, aantal_vergeten, aantal_gebruikte





verplicht = {'python', 'world', 'hello', 'java'}
print(vergeten_woorden('hello 5WWI1', verplicht))