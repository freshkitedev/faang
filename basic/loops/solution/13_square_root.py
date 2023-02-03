# write a program to find square root of given number......
# without using inbuild function......

def squareroot(n):
    b = 0
    if(n > 0):
        b = n**0.5
        return b
    return -1


import unittest

class Test(unittest.TestCase):
    def testsum1(self):
        actual = squareroot (32)
        expected = 5.656854249492381
        self.assertEqual(actual, expected)
    def testsum2(self):
        actual =squareroot (12566)
        expected = 112.09817126073021
        self.assertEqual(actual, expected)
    def testsum3(self):
        actual = squareroot(17875)
        expected = 133.69741957120937
        self.assertEqual(actual, expected)
    def testsum4(self):
        actual = squareroot (-7960)
        expected = -1
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
    