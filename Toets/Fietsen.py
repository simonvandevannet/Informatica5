vs = int(input('snelheid Stijn: '))
vk = int(input('snelheid Kaat: '))
afstand = int(input('afstand: '))
tijd = 1
vs1 = vs
vk1 = vk

while vs + vk < afstand:
    vs, vk = vs + vs1, vk + vk1
    tijd += 1

print('Na {} s hebben Stijn en Kaat elkaar ontmoet.'.format(tijd))