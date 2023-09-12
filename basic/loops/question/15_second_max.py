# Write Program to find second maximum number in list
def second_max_num_in_list(arr):
   
    return max              

import unittest

class Test(unittest.TestCase):
    def test_search1(self):
        actual = max_num_in_list([3,42,34,5,2])
        expected = 34
        self.assertEqual(actual, expected)
    def test_search2(self):
        actual = max_num_in_list([34,9,3,4,-1,-34])
        expected = 9
        self.assertEqual(actual, expected)
    def test_search3(self):
        actual = max_num_in_list([34,9,3,4,-1,-34,98])
        expected = 34
        self.assertEqual(actual, expected)
    def test_search4(self):
        actual = max_num_in_list([1])
        expected = -1
        self.assertEqual(actual, expected)
    def test_search5(self):
        actual = max_num_in_list([-2,-1,0])
        expected = -1
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)