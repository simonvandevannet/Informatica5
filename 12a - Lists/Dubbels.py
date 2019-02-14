def dubbels(lijst):
    dubbels = []
    for i in range(len(lijst)):
        if lijst.count(lijst[i]) > 1 and lijst[i] not in dubbels:
            dubbels.append(lijst[i])
    return dubbels

print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris']))