# Write a function that takes in a non-empty array of distinct integers and an integer 
# representing a target sum.  
# If any two numbers in the input array sum up to the target sum, the function should 
# return them in an array, # in any order.  
# If no two numbers sum up to the target sum, the function should return an empty array.

# O(n^2) time | O(1) space
def two_num_sum(array, targetsum): 
    #Practise yourself : write your code here 
    return []

# O(n) time | O(n) space
def two_num_sum2(array, targetsum): 
    #Practise yourself : write your code here 
    return []

# O(nlogn) time | O(1) space
def two_num_sum3(array, targetsum): 
    #Practise yourself : write your code here 
    return []

import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        actual = two_num_sum(array, 10)
        expected = [11,-1]
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        array = [4,6,1,-2]
        actual = two_num_sum(array, 3)
        expected = []
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = two_num_sum(array, 17)
        expected = [8,9]
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        array = [3]
        actual = two_num_sum(array, 3)
        expected = []
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
