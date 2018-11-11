# uitvoer
n = int(input('n = '))
uitv = 1
v1uitv = 0
# rij van Fibonacci
for _ in range(n - 1):
    v2uitv = v1uitv
    v1uitv = uitv
    uitv = v1uitv + v2uitv

# uitvoer
print(uitv)