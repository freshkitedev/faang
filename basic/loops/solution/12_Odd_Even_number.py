# write a program to find sum of odd and even digits and difference between odd and even.....


def sumofoddeven(n):
    odd = 0
    even = 0
    while n>0:
        rem=n%10
        if rem % 2 == 0:
            even= even + rem
        else:
            odd = odd +rem
        n = n//10
        
    diff = odd-even
    if diff < 0:
        diff=diff * (-1)
    return (odd,even,diff)
    
print(sumofoddeven(165834))
import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = sumofoddeven(165834)
        expected = (9,18,9)
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = sumofoddeven(655326)
        expected = (13,14,1)
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = sumofoddeven(454298)
        expected = (14,18,4)
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = sumofoddeven(87532)
        expected = (15,10,5)
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
