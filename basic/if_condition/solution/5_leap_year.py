#write a program to find leap year


def leap_year(n):
    
    if n%4==0 and n%100!=0: 
        return "leapyear"
    elif n%400==0:
        return "leapyear"
    else:
        return "not a leap year"
        
    

import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = leap_year(1700)
        expected = "not a leap year"
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = leap_year(1935)
        expected = "not a leap year"
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = leap_year(1600)
        expected = "leapyear"
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = leap_year(2008)
        expected = "leapyear"
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)