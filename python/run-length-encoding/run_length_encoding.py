def decode(string):
    result = ''
    number = ''
    for i in range(len(string)):
        if not string[i].isalpha() and not string[i].isspace():
            number += string[i]
        else:
            if number == '':
                result += string[i]
            else:
                result += int(number) * string[i]
                number = ''
    return result


def encode(string):
    if string == "":
        return ""
    counter = 0
    result = ""
    for i in range(len(string) -1):
        letter = string[i]
        if string[i] == string[i+1]:
            counter += 1
        else:
            if counter > 0:
                counter += 1
                result += str(counter) + letter
                counter = 0
            else:
                result += letter
    counter += 1
    if counter > 1:
        result += str(counter) + string[-1]
    else:
        result += string[-1]
    return result

