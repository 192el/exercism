def score(x, y):
    raio = (x**2 + y**2)**0.5
    if raio > 10:
        return 0
    elif raio > 5:
        return 1
    elif raio > 1:
        return 5
    elif raio <= 1:
        return 10
