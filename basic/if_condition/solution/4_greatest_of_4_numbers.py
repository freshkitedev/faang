# Write a program to find the greatest of 4 numbers.

def greatest_of_four(a, b, c, d):
   #Practise yourself : write your code here
    if a>b and a>c and a>d:
        return a
    elif b>c and b>d:
        return b
    elif c>d:
        return c
    return d
import unittest

class Test(unittest.TestCase):
    def test_greatest_of_four(self):
        actual = greatest_of_four(5,10,3,2)
        expected = 10
        self.assertEqual(actual, expected)
    def test_greatest_of_four(self):
        actual = greatest_of_four(7,-3,-10,3)
        expected = 7
        self.assertEqual(actual, expected)
    def test_greatest_of_four(self):
        actual = greatest_of_four(11,2,33,5)
        expected = 33
        self.assertEqual(actual, expected)
    
unittest.main(verbosity=2)