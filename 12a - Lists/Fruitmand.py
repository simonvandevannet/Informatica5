def fruitstuk_toevoegen(fruit, nieuwfruit):
    i = 0

    while  i <= len(fruit) and len(nieuwfruit) > len(fruit[i]):
        i += 1

    if i == len(fruit) and len(nieuwfruit) == len(fruit[i]):
        fruit[i] = nieuwfruit

    elif i == len(fruit):
        fruit.append(nieuwfruit)

    else:
        if len(fruit[i]) == len(nieuwfruit):
            fruit[i] = nieuwfruit
        else:
            fruit = fruit[:i] + [nieuwfruit] + fruit[i:]

    return fruit

print(fruitstuk_toevoegen(['bes', 'peer', 'framboos'],'sinaasappel'))