def gcd(n1, n2):
    gcd = n1
    if (n2 < n1):
        gcd = n2
    while(gcd != 1):
        if(n1 %gcd  == 0 and n2 % gcd == 0):
            return gcd
        gcd -= 1
    return -1  

import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = gcd(34,98)
        expected = 2
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = gcd(34,56)
        expected = 2
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = gcd(4,8)
        expected = 4
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = gcd(45,85)
        expected = 5
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
