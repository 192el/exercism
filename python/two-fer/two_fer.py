import re
default = 'you'
def two_fer(name=default):
    if name is default:
        return 'One for you, one for me.'
    if re.search('[a-zA-z]', name):
        return f'One for {name}, one for me.'
    else:
        return 'One for you, one for me.'
