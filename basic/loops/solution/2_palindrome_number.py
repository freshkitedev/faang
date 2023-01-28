# Write a program to a given number is palindrome or not.
# If the given number is Palindrome return Palindrome (or) 
# the given number is Not Palindrome return Not Palindrome.

def palindrome(n):
    num = n
    pal = rem = 0
    while (num):
        rem = num % 10
        pal = rem + pal * 10
        num //= 10
    if n == pal:
        return "Palindrome"
    else:
        return "Not Palindrome"

import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = palindrome(159357)
        expected = "Not Palindrome"
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = palindrome(63636)
        expected = "Palindrome"
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = palindrome(45)
        expected = "Not Palindrome"
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = palindrome(8)
        expected = "Palindrome"
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
