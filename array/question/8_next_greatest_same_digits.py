# Write an algorithm to find out next greater number to given number with the same set of digits 
# Asked in : Morgan Stanley, Makemytrip, Amazon

def next_max_num(val):
    # code here

import unittest
class Test(unittest.TestCase):
  
    def test_next_big_num(self):
        actual = next_max_num(15843)
        expected = 18345
        self.assertEqual(actual, expected)

    def test_next_big_num1(self):
        actual = next_max_num(13)
        expected = 31
        self.assertEqual(actual, expected)
    
    def test_next_big_num2(self):
        actual = next_max_num(13843)
        expected = 14338
        self.assertEqual(actual, expected)

    def test_next_big_num3(self):
        actual = next_max_num(12345)
        expected = 12354
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
