def steps(number):
    stepstaken = []
    if number > 0:
        while number > 1:
            if number % 2 == 0:
                number = number / 2
                stepstaken.append(1)
            else:
                number = (number * 3) + 1
                stepstaken.append(1)
        return sum(stepstaken)
    else:
        raise ValueError("Only positive integers are allowed")