def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquotsum = []
    if number > 0:
        for i in range(1, number):
            if number % i == 0:
                aliquotsum.append(i)
        if number == sum(aliquotsum):
            return 'perfect'
        elif number < sum(aliquotsum):
            return 'abundant'
        elif number > sum(aliquotsum):
            return 'deficient'
    else:
        raise ValueError("Classification is only possible for positive integers.")
