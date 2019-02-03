def vlag(richting, kleuren):
    vlag = ''

    if richting == 'verticaal':
        while len(kleuren) != 0:
            vlag += kleuren[0] + ' | '
            kleuren = kleuren[1:]
        vlag = vlag[0:-3]

    if richting == 'horizontaal':
        while len(kleuren) != 0:
            vlag += kleuren[0] + '\n' + '-' + '\n'
            kleuren = kleuren[1:]
        vlag = vlag[0:-3]

    return vlag