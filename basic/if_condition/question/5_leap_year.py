#write a program to find leap year

def leap_year(n):
    
   #Write here

     return 
import unittest

class Test(unittest.TestCase):
    def find_leap_year(self):
        actual = leap_year(1700)
        expected ="leapyear"
        self.assertEqual(actual, expected)
    def find_leap_year(self):
        actual = leap_year(2018)
        expected ="not a leap year"
        self.assertEqual(actual, expected)
    def find_leap_year(self):
        actual = leap_year(2020)
        expected ="leapyear"
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)