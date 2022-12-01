def encode(plain_text):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('1234567890')
    ALPHABET = [letter.upper() for letter in alphabet]
    tebahpla = list('zyxwvutsrqponmlkjihgfedcba')
    plain_test = [letter for letter in plain_text if letter in (numbers + alphabet + ALPHABET)]
    encoded = ''
    encodedwordlenght = 0
    for letter in plain_text:
        if letter in alphabet or letter in ALPHABET:
            encoded = encoded + tebahpla[alphabet.index(letter.lower())]
            encodedwordlenght += 1
        if letter in numbers:
            encoded = encoded + letter
            encodedwordlenght += 1
        if encodedwordlenght == 5:
            encoded = encoded + ' '
            encodedwordlenght = 0
    return encoded.strip()


def decode(ciphered_text):
    ciphered_text = encode(ciphered_text)
    return ciphered_text.replace(' ', '')
