
# generate the first n primes and return the nth prime
def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    primes = [2]
    candidate = 3
    while len(primes) <= number:
        if all(candidate % p != 0 for p in primes):
            primes.append(candidate)
        candidate += 1
    return primes[-2]

