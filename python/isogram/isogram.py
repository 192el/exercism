def is_isogram(string):
    string = string.lower()
    lower_case_letters = list("abcdefghijklmnopqrstuvwxyz")
    onlyletters = [letter for letter in string if letter in lower_case_letters]
    onlyletters = sorted(onlyletters)
    removedrepeats = []
    [removedrepeats.append(letter) for letter in onlyletters if letter not in removedrepeats]
    if removedrepeats == onlyletters:
        return True
    else:
        return False