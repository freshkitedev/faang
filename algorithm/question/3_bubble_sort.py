# complete below function to return the sorted array - Bubble sort


def bubble_sort(arr):
    pass

def bubble_sort_efficient(arr):
    pass


import unittest

class Test(unittest.TestCase):
    def test_search1(self):
        actual = bubble_sort([3,42,34,5,2])
        expected = [2,3,5,34,42]
        self.assertEqual(actual, expected)
    def test_search2(self):
        actual = bubble_sort([34,9,3,4,-1,-34])
        expected = [-34,-1,3,4,9,34]
        self.assertEqual(actual, expected)
    def test_search3(self):
        actual = bubble_sort([34,9,3,4,-1,-34])
        expected = [-34,-1,3,4,9,34]
        self.assertEqual(actual, expected)
    def test_search3(self):
        actual = bubble_sort([1,2,3,4,5])
        expected = [1,2,3,4,5]
        self.assertEqual(actual, expected)
    def test_search4(self):
        actual = bubble_sort([])
        expected = []
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)