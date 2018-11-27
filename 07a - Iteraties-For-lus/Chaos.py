# invoer
d = float(input('initiële populatiedichtheid: '))
r = float(input('vruchtbaarheidsparameter: '))
s = int(input('aantal tijdsstappen: '))

# berekening
print(d)
for i in range(s - 1):
    i = r * d * (1 - d)
    d = i
    print(i)

