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



# oplossing
n = int(input('hoeveelste getal van Fibonacci'))

vorige = 1
huidige = 1
# vorige, huidige = 1,1

for i in range(n - 2):
    vorige, huidige = huidige, huidige + vorige

print(huidige)