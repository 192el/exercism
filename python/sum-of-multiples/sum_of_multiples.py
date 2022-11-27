def sum_of_multiples(limit, multiples):
    result = []
    if 0 in multiples:
        multiples.remove(0)
    if multiples == []:
        return 0
    else:
        for i in range(limit):
            for y in range(len(multiples)):
                if i % multiples[y] == 0:
                    if i not in result:
                        result.append(i)
    return sum(result)
