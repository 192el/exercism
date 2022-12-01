def translate(text):
    resultado = []
    for palavra in text.split():
        if palavra[0] in ['a', 'e', 'i', 'o', 'u']:
            palavra = palavra
        elif palavra[:3] in ['squ', 'thr', 'sch']:
            palavra = palavra[3:] + palavra[:3]
        elif palavra[:2] in ['yt', 'xr', 'sq']:
            palavra = palavra
        elif palavra[:2] in ['ch', 'qu', 'th', 'rh']:
            palavra = palavra[2:] + palavra[:2]
        else:
            palavra = palavra[1:] + palavra[0]
        palavra += 'ay'
        resultado.append(palavra)
    return ' '.join(resultado)
