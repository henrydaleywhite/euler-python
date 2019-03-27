"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def get_max_prime_factor(number):
    """return the largest prime factor of a given number"""
    factors = get_prime_factors(number)
    return max(factors)


def get_prime_factors(number):
    """return the prime factors of a given number"""
    num_to_div = number
    prime_factors = set()
    num_to_test = 2
    while num_to_test <= num_to_div:
        if num_to_div % num_to_test == 0:
            prime_factors.add(num_to_test)
            num_to_div /= num_to_test
        else:
            num_to_test += 1
    return prime_factors


if __name__ == "__main__":
    print(get_max_prime_factor(600851475143))