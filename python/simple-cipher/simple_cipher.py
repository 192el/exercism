from random import randint
class Cipher(object):
    def __init__(self, key=None):
        if key == None:
            self.key = "".join([chr(randint(ord('a'), ord('z'))) for i in range(100)])
        elif key.lower() != key or not key.isalpha():
            raise ValueError
        else:
            self.key = key
    def shift(self, i):
        return ord(self.key[i % len(self.key)]) - ord('a')
    def encode(self, message):
        encoded = []
        for i, ch in enumerate(message):
            if ch.isalpha():
                ch = ch.lower()
                shift = self.shift(i)
                encoded.append(chr( (ord(ch) - ord('a') + shift) % 26 + ord('a')) )
        return "".join(encoded)
    def decode(self, message):
        decoded = []
        for i, ch in enumerate(message):
            shift = self.shift(i)
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            decoded.append(chr( (ord(ch) - ord('a') - shift) % 26 + ord('a') ) )
        return "".join(decoded)