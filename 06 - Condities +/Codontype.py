# invoer
codon = input('Geef codon: ')

# berekening
if len(codon) == 3:
    if codon == 'AUG':
        codontype = 'start codon'
    elif codon == 'UAG' or codon == 'UGA' or codon == 'UAA':
        codontype = 'stop codon'
    else:
        codontype = 'gewoon codon'
else:
    codontype = 'ongeldig codon'

# uitvoer
print('Het codon ' + codon + ' is een ' + codontype + '.')