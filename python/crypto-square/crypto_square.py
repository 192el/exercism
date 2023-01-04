def cipher_text(plain_text):
    plain_text = plain_text.lower()
    plain_text = ''.join(letter for letter in plain_text if letter.isalnum())
    ciphertext = ''
    lenght = len(plain_text)
    rows = round(len(plain_text) ** 0.5)
    if lenght > rows * rows:
        columns = rows + 1
    else:
        columns = rows
    for i in range(columns):
        for j in range(rows):
            try:
                ciphertext += plain_text[i + j * columns]
            except IndexError:
                ciphertext += " "
        ciphertext += " "
    ciphertext = ciphertext[:-1]
    return ciphertext

