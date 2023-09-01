# write a program to find sum of digits of an integer..


def Prime(n):
   for i in range(2,10):
        if(i == n):
            break 
        if(n % i == 0):
            return "Not Prime number"
        
   return "Prime number"


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