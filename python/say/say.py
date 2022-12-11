def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    if say_billions(number).endswith("-"):
        return say_billions(number).strip().replace("-", "")
    else:
        return say_billions(number).strip()

def say_billions(number):
    if number < 1000000000:
        return say_millions(number)
    return say_hundreds(number // 1000000000) + " billion " + say_millions(number % 1000000000)

def say_millions(number):
    if number < 1000000:
        return say_thousands(number)
    return say_hundreds(number // 1000000) + " million " + say_thousands(number % 1000000)

def say_thousands(number):
    if number < 1000:
        return say_hundreds(number)
    return say_hundreds(number // 1000) + " thousand " + say_hundreds(number % 1000)





def say_hundreds(number):
    if number < 100:
        return say_tens(number)
    return say_units(number // 100) + " hundred " + say_tens(number % 100)

def say_tens(number):
    if number < 10:
        return say_units(number)
    if number < 20:
        return say_teens(number)
    return say_tens_units(number // 10) + say_units(number % 10)

def say_teens(number):
    return {
        10: "ten-",
        11: "eleven-",
        12: "twelve-",
        13: "thirteen-",
        14: "fourteen-",
        15: "fifteen-",
        16: "sixteen-",
        17: "seventeen-",
        18: "eighteen-",
        19: "nineteen-",
    }[number]

def say_tens_units(number):
    return {
        2: "twenty-",
        3: "thirty-",
        4: "forty-",
        5: "fifty-",
        6: "sixty-",
        7: "seventy-",
        8: "eighty-",
        9: "ninety-",
        0: "",
    }[number]

def say_units(number):
    return {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "",
    }[number]


