# write a program to find sum of digits of an integer.......


def sum_of_digit(n):
    #write your code here


    
print(sum_of_digit(n))


import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = sum_of_digit(123)
        expected = 6
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = sum_of_digit(123456789)
        expected = 45
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = sum_of_digit(45)
        expected = 9
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = sum_of_digit(4)
        expected = 4
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
