def is_valid(isbn):
    lista = list(isbn)
    digits = []
    resultorsomeshit = []
    stringsdigits = list("0123456789")
    stringsdigits.append("10")
    if len(lista) == 0:
        return False
    elif isbn.endswith('X'):
        lista.pop()
        lista.append("10")
    elif lista[-1] not in stringsdigits:
        return False
    lista = [item for item in lista if item != "-"]
    if len(lista) != 10 and lista[-1] != "10":
        return False
    else:
        for i in range(len(lista)):
            if lista[i] in stringsdigits:
                if lista[i] in stringsdigits:
                    digits.append(int(lista[i]))
        for i in range(len(digits)):
            if digits[i] != 0:
                resultorsomeshit.append(digits[i] * (10 - i))
        if sum(resultorsomeshit) % 11 == 0:
            return True
        else:
            return False