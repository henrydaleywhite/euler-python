"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def get_primes(max_len):
    """return the first n prime numbers"""
    prime_list = [2]
    number_to_check = 3
    while len(prime_list) < max_len:
        for prime in prime_list:
            prime_state = True
            if number_to_check % prime == 0:
                prime_state = False
                break
        if prime_state:
            prime_list.append(number_to_check)
        number_to_check += 1
    return prime_list


if __name__ == '__main__':
    print(get_primes(10001)[-1])