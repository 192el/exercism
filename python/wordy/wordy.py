def answer(question):
    question = question[:-1]
    lista = question.split(" ")
    lista[-1].replace("?", "")
    knownoperators = ["plus", "minus", "multiplied by", "divided by"]
    operations = [item for item in lista if item in knownoperators]
    lista = [item if item != 'divided' else 'divided by' for item in lista]
    lista = [item if item != 'multiplied' else 'multiplied by' for item in lista]
    lista = [item for item in lista if item != 'by']
    if 'cubed' in lista or not 'What' in lista:
        raise ValueError("unknown operation")
    if len(lista) == 3:
        return int(lista[-1])
    lista = [item for item in lista if item not in ['What', 'is']]
    return calculatormaybe(lista)

def calculatormaybe(lista):
    try:
        if lista[1] == 'plus':
            result = float(lista[0]) + float(lista[2])
        elif lista[1] =='minus':
            result = float(lista[0]) - float(lista[2])
        elif lista[1] =='multiplied by':
            result = float(lista[0]) * float(lista[2])
        elif lista[1] =='divided by':
            result = float(lista[0]) / float(lista[2])
        if len(lista) == 3:
            return result
        if len(lista) > 3:
            lista = [result, lista[-2], lista[-1]]
            return calculatormaybe(lista)
    except:
        raise ValueError('syntax error')