# complete below function to return the index
# of number n in arr - Linear search - O(n)

def search(arr, n):
    for i in range(len(arr)):
        if n == arr[i]:
            return i
    return -1

import unittest

class Test(unittest.TestCase):
    def test_search1(self):
        actual = search([3,42,34,5,2], 34)
        expected = 2
        self.assertEqual(actual, expected)
    def test_search2(self):
        actual = search([4,42,3,42,34,5,2], 42)
        expected = 1
        self.assertEqual(actual, expected)
    def test_search3(self):
        actual = search([3,42,34,5,2], 6)
        expected = -1
        self.assertEqual(actual, expected)
    def test_search4(self):
        actual = search([], 6)
        expected = -1
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)