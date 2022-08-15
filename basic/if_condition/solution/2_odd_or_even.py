# Write a program to check a number is odd or even.
#If the number is odd you should return the ans variable set to "ODD".
#If the number is even you should return the ans variable set to "EVEN".
#If the input number is 0 or negative return the ans variable set to "INVALID NUMBER"
#Complete the function below and store your result in ans variable
def odd_or_even(num):
    ans = " "
   #Practise yourself : write your code here
    if num <= 0:
        ans = "INVALID NUMBER" 
    else:
        if num%2 == 0:
            ans = "EVEN"
        else:
            ans = "ODD"

    return ans
import unittest

class Test(unittest.TestCase):
    def test_odd_or_even(self):
        num = 5
        actual = odd_or_even(num)
        expected = "ODD"
        self.assertEqual(actual, expected)
    def test_odd_or_even(self):
        num = 2
        actual = odd_or_even(num)
        expected = "EVEN"
        self.assertEqual(actual, expected)
    def test_odd_or_even(self):
        num = 0
        actual = odd_or_even(num)
        expected = "INVALID NUMBER"
        self.assertEqual(actual, expected)
    def test_odd_or_even(self):
        num = -5
        actual = odd_or_even(num)
        expected = "INVALID NUMBER"
        self.assertEqual(actual, expected)
    
unittest.main(verbosity=2)

