def lcm(x, y):
    if x > y:
       great = x
    else:
         great = y

    while(True):
       if((great % x == 0) and (great % y == 0)):
           lcmoftwono = great
           break
       great += 1
    return lcmoftwono
   
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

   