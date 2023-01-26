# Write a program to swap first and last digit in a given number

def swapFirstLast(n):
    #code here
    a = 0
    return a

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
