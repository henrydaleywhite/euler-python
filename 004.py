"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindromic_number(max_num):
    """find the greatest palindromic number from the
    product of two numbers with a max size parameter
    """
    adj_num = max_num
    cur_max = 0
    for i in range(max_num, max_num // 2, -1):
        for j in range(adj_num, adj_num // 2, -1):
            num_to_check = adj_num * j
            if check_palindrome(num_to_check):
                if num_to_check > cur_max:
                    cur_max = num_to_check
        adj_num -= 1
    return cur_max    


def check_palindrome(number):
    """check if a number is a palindrome"""
    str_num = str(number)
    for i in range(len(str_num) // 2):
        if str_num[i] != str_num[-(i + 1)]:
            return False
    return True


if __name__ == '__main__':
    print(palindromic_number(999))