"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math


def smallest_divis_number(max_num):
    """return the smallest positive number evenly
    divisible by numbers from 1 to max_num
    """
    # FIXME make this significantly better
    denoms = get_primes(max_num)
    num_to_test = 230000000
    while True:
        divis = True
        for number in denoms[::-1]:
            if num_to_test % number != 0:
                divis = False
                break
        if divis:
            return num_to_test
        print(num_to_test)
        num_to_test += max_num


def get_primes(max_num):
    """return list of all prime numbers up to and including max_num"""
    prime_list = []
    for num in range(2, max_num + 1):
        prime = True
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                prime = False
                break
        if prime:
            prime_list.append(num)
    return prime_list


if __name__ == "__main__":
    print(smallest_divis_number(20))
    # from numpy import prod
    # print(prod(get_primes(20)))