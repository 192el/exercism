def response(hey_bob):
    hey_bob.replace(" ", "")
    if hey_bob == hey_bob.upper() and hey_bob.endswith("?") and hey_bob.upper() != hey_bob.lower():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.endswith("?"):
        return "Sure."
    elif hey_bob == hey_bob.upper() and not hey_bob.endswith("?") and hey_bob.upper() != hey_bob.lower():
        return "Whoa, chill out!"
    elif hey_bob == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
