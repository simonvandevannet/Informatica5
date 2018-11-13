# invoer
n = int(input('n = '))
uitvoer = 1
uitvoer1 = 0

# berekening
for _ in range(n - 1):
    uitvoer2 = uitvoer1
    uitvoer1 = uitvoer
    uitvoer = uitvoer1 + uitvoer2

# uitvoer
print(uitvoer)