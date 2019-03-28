"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math


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
    print(sum(get_primes(2000000)))