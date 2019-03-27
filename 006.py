"""The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def square_sum(first, last):
    """get the square of the sum of a range of
    numbers given the first and last number
    """
    range_numbers = range(first,last + 1)
    square_sum = sum(range_numbers) ** 2
    return square_sum


def sum_squares(first, last):
    """get the sum of the squares of a range of
    numbers given the first and last number
    """
    range_numbers = range(first,last + 1)
    sum_squares = 0
    for number in range_numbers:
        sum_squares += number ** 2
    return sum_squares


def sq_sum_less_sum_sq(sum_squares, square_sum):
    """difference of sum of squares and squared sum of a range of numbers"""
    return sum_squares - square_sum


if __name__ == '__main__':
    res_square_sum = square_sum(1, 10)
    res_sum_squares = sum_squares(1, 10)
    answer = sq_sum_less_sum_sq(res_square_sum, res_sum_squares)
    print(answer)