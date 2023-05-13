def gcd(n1, n2):
    gcd = n1 
    big = n1
    if n1>n2:
        gcd = n2 
    else:
        big = n2
    small = gcd 
    d=2
    while(big % gcd!=0): 
            if small % d == 0:
                gcd = small //d
            d+=1
    return gcd 
 
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
