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
    def leap_year(self):
        actual = leap_year(1700)
        expected ="leapyear"
        self.assertEqual(actual, expected)
    def leap_year(self):
        actual = leap_year(2018)
        expected ="not a leap year"
        self.assertEqual(actual, expected)
    def leap_year(self):
        actual = leap_year(2020)
        expected ="leapyear"
        self.assertEqual(actual, expected)
    def leap_year(self):
        actual = leap_year(1990)
        expected = "not a leap year"
        self.assertEqual(actual, expected)
    def leap_year(self):
        actual = leap_year(1992)
        expected = "leapyear"
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)