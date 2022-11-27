def flatten(iterable):
    unnested = []
    for i in iterable:
        if type(i) == int or type(i) == float:
            unnested.append(i)
        elif type(i) == list:
            unnested = unnested + flatten(i)
    return unnested
