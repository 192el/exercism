from math import ceil
def rows(letter):
    alphabet = {"A": 1, "B": 3, "C": 5, "D": 7, "E": 9, "F": 11, "G": 13, "H": 15, "I": 17, "J": 19, "K": 21, "L": 23, "M": 25, "N": 27, "O": 29, "P": 31, "Q": 33, "R": 35, "S": 37, "T": 39, "U": 41, "V": 43, "W": 45, "X": 47, "Y": 49, "Z": 51}
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    result = []
    if letter == "A":
        return ["A"]
    middle1 = ceil(alphabet[letter] / 2)
    middle2 = ceil(alphabet[letter] / 2)
    for i in range(ceil(alphabet[letter] / 2)):
        temp = ""
        for y in range(alphabet[letter]):
            if i == 0:
                if y == middle1 - 1:
                    temp += letters[i]
                else:
                    temp += " "
            else:
                if y == middle1 - 1 or y == middle2 - 1:
                    temp += letters[i]
                else:
                    temp += " "
        result.append(temp)
        middle1 -= 1
        middle2 += 1
    for i in range(len(result) - 2, -1, -1):
        result.append(result[i])
    return result

