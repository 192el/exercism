def is_pangram(sentence):
    sentence = sentence.lower()
    set(sentence)
    lower_case_letters = list('abcdefghijklmnopqrstuvwxyz')
    pangram = True
    for letter in lower_case_letters:
        if letter not in sentence:
            pangram = False
    return pangram