#input
a = float(input('Geef  bedrag in cent: '))

#output
aantal_muntstukken = str(a) + str(' cent kan je omwisselen in ')
aantal_muntstukken += str((a // 100)+((a%100)//50)+((a%50)//20)+(((a%50)%20)//10)+((((a%50)%20)%10)//5)+(((((a%50)%20)%10)%5)//2)+((((((a%50)%20)%10)%5)%2)//1))
aantal_muntstukken += str(' muntstukken')
print(aantal_muntstukken)