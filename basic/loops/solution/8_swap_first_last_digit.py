# Write a program to swap first and last digit in a given number

def count_digits(n):
    count = 0
    while (n):
        count += 1
        n //= 10
    return count

def swapFirstLast(n):
    c = count_digits(n)
    if c == 1:
        return n

    ld = n % 10
    p = 10 ** (c - 1)
    fd = n // p

    n = n % p
    n //= 10

    n = n * 10 + fd
    ld *= p
    n = ld + n
    return n


import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = swapFirstLast(456)
        expected = 654
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = swapFirstLast(456493)
        expected = 356494
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = swapFirstLast(45)
        expected = 54
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = swapFirstLast(4)
        expected = 4
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
