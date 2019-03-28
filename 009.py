"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

# Euclid's
# When m and n are any two positive integers (m < n):
# a = n^2 - m^2
# b = 2nm
# c = n^2 + m^2

from numpy import prod


def iterate_m_n_values(abc_sum):
    """iterate over possible values of m and n to 
    get a + b + c equal to the abc_sum parameter
    """
    a, b, c = 0, 0, 0
    m = 0
    n = 2
    while a + b + c != abc_sum:
        if m + 1 == n:
            m = 1
            n += 1
        else:
            m += 1
        a = calc_a(m, n)
        b = calc_b(m, n)
        c = calc_c(m, n)
    return (a, b, c)


def calc_a(var_m, var_n):
    """calc a with formula a = n^2 - m^2"""
    return var_n**2 - var_m**2


def calc_b(var_m, var_n):
    """calc b with formula b = 2nm"""
    return 2 * var_n * var_m


def calc_c(var_m, var_n):
    """calc c with formula c = n^2 + m^2"""
    return var_n**2 + var_m**2


def product_abc(abc_list):
    """return the product of a list containing a pythagorean triple"""
    return prod(abc_list)


if __name__ == "__main__":
    pyth_triple = iterate_m_n_values(1000)
    print(product_abc(pyth_triple))