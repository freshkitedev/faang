# complete below function to return the sorted array - Bubble sort


def max_num_in_list(arr):
    pass

def max_num_in_list_efficient(arr):
    pass


import unittest

class Test(unittest.TestCase):
    def test_search1(self):
        actual = max_num_in_list([3,42,34,5,2])
        expected = [2,3,5,34,42]
        self.assertEqual(actual, expected)
    def test_search2(self):
        actual = max_num_in_list([34,9,3,4,-1,-34])
        expected = [-34,-1,3,4,9,34]
        self.assertEqual(actual, expected)
    def test_search3(self):
        actual = max_num_in_list([34,9,3,4,-1,-34])
        expected = [-34,-1,3,4,9,34]
        self.assertEqual(actual, expected)
    def test_search3(self):
        actual = max_num_in_list([1,2,3,4,5])
        expected = [1,2,3,4,5]
        self.assertEqual(actual, expected)
    def test_search4(self):
        actual = max_num_in_list([])
        expected = []
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)