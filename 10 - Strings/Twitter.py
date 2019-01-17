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

tweet = input('geef tweet: ')

i_hashtag = tweet.find('#')

while i_hashtag != -1:

    # tweet afknippen net na het #-teken
    tweet = tweet[i_hashtag + 1:]
    i_spatie = tweet.find(' ')

    # hashtag uitknippen (en printen)
    print(tweet[:i_spatie])

    # terug op zoek naar een #
    i_hashtag = tweet.find('#')