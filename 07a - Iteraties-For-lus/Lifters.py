n = int(input('aantal lifters: '))
max = float(input('score: '))

for i in range(n - 1):
    s = float(input('score: '))

for i in range(n // 2):
    if s > max:
        max = s

for i in range(n // 2, n + 1):
    if s > max:
        print(s)
    else:
        print('lol')