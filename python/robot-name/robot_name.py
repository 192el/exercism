class Robot:
    def __init__(self):
        self.reset()


    def reset(self):
        self.name = next(NAMES)



from itertools import product
from string import ascii_uppercase as uppercase

letters = (''.join(x) for x in product(uppercase, repeat=2))
numbers = (str(i).zfill(3) for i in range(1000))
allnames = [l + n for l, n in product(letters, numbers)]
NAMES = iter(allnames)