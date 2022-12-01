def score(word):
    lettervalues = {}
    lettervalues.update(dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1))
    lettervalues.update(dict.fromkeys(['D', 'G'], 2))
    lettervalues.update(dict.fromkeys(['B', 'C', 'M', 'P'], 3))
    lettervalues.update(dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4))
    lettervalues.update(dict.fromkeys(['K'], 5))
    lettervalues.update(dict.fromkeys(['J', 'X'], 8))
    lettervalues.update(dict.fromkeys(['Q', 'Z'], 10))
    total = []
    for letter in word:
        total.append(lettervalues[letter.upper()])
    return sum(total)