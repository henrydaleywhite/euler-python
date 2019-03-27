"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_mul_three_five(max_num):
    """returns the sum of all of the multiples of
    three or five up to the max number parameter
    """
    answer = set()
    for i in range(max_num):
        if i % 3 == 0 or i % 5 == 0:
            answer.add(i)
    return sum(answer)


if __name__ == "__main__":
    print(sum_mul_three_five(1000))