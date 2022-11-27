def abbreviate(words):
    words.replace('-', ' ')
    words.replace('_', ' ')
    letters = list(words)
    acronym = [letters[0]]
    for i in range(len(letters)):
        if letters[i] == ' ':
            acronym.append(letters[i+1])
    result = ''.join(acronym)
    return result.upper()
