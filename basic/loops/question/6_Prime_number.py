# Write a program to find a number is prime number or not.

def Prime(n):
    #write code here
    
    return 


import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = Prime(13)
        expected = "Prime number"
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = Prime(101)
        expected = "Prime number"
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = Prime(100)
        expected = "Not Prime number"
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = Prime(4)
        expected = "Not Prime number"
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)