zin = input('zin: ')
hashtag = ''

for i in range(0, len(zin)):
    if zin[i] == '#':
        plaatsh = i
        while zin[i] != ' ':
            i += 1
        plaatss = i
        hashtag += zin[plaatsh + 1: plaatss] + '\n'

print(hashtag)