def boot_overlappend(toevoeging, boten):
    return len(toevoeging.intersection(boten)) > 0

def boot_toevoegen(toevoeging, boten):
    if boot_overlappend(toevoeging, boten) == False:
        totaal = toevoeging.union(boten)
    else:
        totaal = boten
    return totaal

def vuur(plaats, boten):
    if plaats in boten:
        mes = True
    else:
        mes = False
    boten.discard(plaats)
    return mes, boten





print(boot_overlappend({'B4', 'A4', 'C4'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(boot_toevoegen({'F4', 'F5', 'F6', 'F3'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(vuur('F8',{'E4', 'H8', 'I8', 'A2', 'G8', 'D4', 'C4', 'F8'}))