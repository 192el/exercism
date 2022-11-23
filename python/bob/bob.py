def response(hey_bob):
    letterlower = set('abcdefghijklmnopqrstuvwxyz?')
    letterupper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
    numbers = set('1234567890')
    if hey_bob == hey_bob.upper() and "?" in list(hey_bob) and hey_bob.upper() != hey_bob.lower():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.strip().endswith("?"):
        return "Sure."
    elif hey_bob == hey_bob.upper() and not hey_bob.endswith("?") and hey_bob.upper() != hey_bob.lower():
        return "Whoa, chill out!"
    elif set(hey_bob).isdisjoint(letterlower) and set(hey_bob).isdisjoint(letterupper) and set(hey_bob).isdisjoint(numbers):
        return "Fine. Be that way!"
    else:
        return "Whatever."
