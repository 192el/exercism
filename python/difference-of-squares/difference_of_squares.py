def square_of_sum(number):
    numbers = []
    for i in range(1, number + 1):
        numbers.append(i)
    return ((sum(numbers)) ** 2)


def sum_of_squares(number):
    numbers = []
    for i in range(1, number + 1):
        numbers.append(i**2)
    return sum(numbers)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
