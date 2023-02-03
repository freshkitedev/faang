#Find the sum of even and odd positioned digits in a number and subtract summed odd and even number.
#Position is if 456493 is our number then the poition is the index 123456 now take the even and odd positioned number and sum them.
#After the summing the odd and even positoned digits in that number just subtract the even and odd result. 

def Odd_even(num):
    odd = 0
    even = 0
    result = 0
    return odd, even, result


import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = Odd_even(456)
        expected = 10, 5, 5
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = Odd_even(456493)
        expected = 19, 12, 7
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = Odd_even(45)
        expected = 4, 5, 1
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = Odd_even(67895432198765)
        expected = 37, 43, 6
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
