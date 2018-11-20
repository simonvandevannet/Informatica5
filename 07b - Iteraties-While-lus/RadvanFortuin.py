# invoer
woord = input('woord: ')
geldbedrag = int(input('bedrag per juiste letter: '))
letter = input('letter: ')
winst = 0
antwoorden = ''

# berekening
while letter in woord and letter not in antwoorden:
    winst += geldbedrag
    antwoorden += letter
    letter = input('letter: ')

# uitvoer
print(winst)