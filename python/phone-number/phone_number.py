def cleanup(number):
    number = number.replace(' ', '').replace('(', '').replace(')', '').replace('-', '').replace('+', '').replace('.', '')
    if len(number) < 10:
        raise ValueError("incorrect number of digits")
    if len(number) == 11 and number[0] != '1':
        raise ValueError("11 digits must start with 1")
    if len(number) > 11:
        raise ValueError("more than 11 digits")
    if len(number) == 10:
        number = '1' + number
    if number[1] == '0':
        raise ValueError("area code cannot start with zero")
    if number[1] == '1':
        raise ValueError("area code cannot start with one")
    if number[4] == '0':
        raise ValueError("exchange code cannot start with zero")
    if number[4] == '1':
        raise ValueError("exchange code cannot start with one")
    if any(char.isalpha() for char in number):
        raise ValueError("letters not permitted")
    if any(char in number for char in '.,;:!@#$%¨&*:?'):
        raise ValueError("punctuations not permitted")
    if number[0] == '1':
        number = number[1:]
    return number


class PhoneNumber:
    def __init__(self, number):
        self.number = cleanup(number)
        self.area_code = self.area_code()

    def pretty(self):
        return f'({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}'

    def area_code(self):
        return self.number[0:3]
