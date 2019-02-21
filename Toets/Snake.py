def beweeg(coordinaten, beweging):
    x = coordinaten[0]
    y = coordinaten[1]
    if beweging == '<':
        x -= 1
    elif beweging == '>':
        x += 1
    elif beweging == '^':
        y += 1
    else:
        y -= 1
    return x, y

def teruggekeerd(lijst):
    return ('^' in lijst and 'v' in lijst) or ('<' in lijst and '>' in lijst)


def laatste_levende_positie(lijst):
    i = 1
    coordinaten = beweeg((0, 0), lijst[0])
    while teruggekeerd(lijst[i - 1 : i + 1]) is False and i < len(lijst):
        coordinaten = beweeg(coordinaten, lijst[i])
        i += 1
    return i, coordinaten[0], coordinaten[1]

print(beweeg((7, 3), '^'))
print(teruggekeerd(['^', 'v']))
print(laatste_levende_positie(['>', '<', '^']))
print(laatste_levende_positie(['v', '>', 'v', '<', '^', '^']))
print(laatste_levende_positie(['>', 'v', '>', '<', '<', '^', 'v', '<', '>', '>', '>', '^']))