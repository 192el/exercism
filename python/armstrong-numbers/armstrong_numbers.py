def is_armstrong_number(number):
    stringnumbers = str(number)
    digits = list(stringnumbers)
    power = len(stringnumbers)
    result = []
    for i in range(len(digits)):
        result.append((int(digits[i]) ** power))
    return sum(result) == number
