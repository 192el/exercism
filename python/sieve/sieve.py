def primes(limit):
    numbers = [i for i in range(2, limit + 1)]
    for i in range(len(numbers)):
        if numbers[i] is not None:
            for j in range(i + numbers[i], len(numbers), numbers[i]):
                numbers[j] = None
    return [i for i in numbers if i is not None]
