def lcm(n1, n2):
    lcm = n2
    if (n1 > n2):
        lcm = n1
    while(True):
        if (lcm % n1 == 0) and (lcm % n2 == 0):
            return lcm
        lcm += lcm
   
import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = lcm(34,98)
        expected = 1666
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = lcm(34,56)
        expected = 952
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = lcm(4,7)
        expected = 28
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = lcm(45,85)
        expected = 765
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)

   