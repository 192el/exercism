def value(colors):
    colorlist = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    lista = []
    for i in range(len(colors)):
        lista.append(colorlist.index(colors[i]))
    str(lista)
    if lista[0] == 0:
        return lista[1]
    else:
        return int(f'{lista[0]}{lista[1]}')
