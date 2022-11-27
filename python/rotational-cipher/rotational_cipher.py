def rotate(text, key):
    if key == 0 or key == 26:
        return text
    lowerletters = list("abcdefghijklmnopqrstuvwxyz")
    upperletters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowercipher = lowerletters[key:] + lowerletters[:key]
    uppercipher = upperletters[key:] + upperletters[:key]
    text = list(text)
    for i in range(len(text)):
        if text[i].isupper():
            text[i] = uppercipher[upperletters.index(text[i])]
        elif text[i].islower():
            text[i] = lowercipher[lowerletters.index(text[i])]
    return ''.join(text)
