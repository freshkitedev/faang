#write a program to a given number is amstrong or not.
n=int(input())
def amstrong(n):
    order=len(str(n))
    sum=0
    num=n
    while(num>0):
        rem=num%10
        sum+=rem**order
        num=num//10
    if n==sum:
        return "amstrong"
    else:
        return "not_amstrong"

import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = amstrong(11)
        expected = "not_amstrong"
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = amstrong(153)
        expected = "amstrong"
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = amstrong(123)
        expected = "not_amstrong"
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = amstrong(370)
        expected = "amstrong"
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
