def abbreviate(words):
    words = words.replace('-', ' ')
    words = words.replace('_', '')
    letters = list(words)
    acronym = [letters[0]]
    for i in range(len(letters)):
        if letters[i] == ' ':
            acronym.append(letters[i+1])
    result = ''.join(acronym)
    result = result.replace(' ', '')
    return result.upper()
