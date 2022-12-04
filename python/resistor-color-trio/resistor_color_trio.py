def label(colors):
    colorlist = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    ohms = []
    ohms.append(str(colorlist.index(colors[0])))
    ohms.append(str(colorlist.index(colors[1])))
    for i in range(colorlist.index(colors[2])):
        ohms.append('0')
    ohm = ''.join(ohms)
    ohm = int(ohm)
    if ohm < 1000:
        return f"{ohm} ohms"
    else:
        kgohm = ohm / 1000
        return f'{int(kgohm)} kiloohms'