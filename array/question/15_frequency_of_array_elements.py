# Function to find counts of all elements present in arr[0..n-1]. The array  elements must be range from 1 to n
def printfrequency(arr, n): 
    #code here

import unittest

class Test(unittest.TestCase):
    def test_printfrequency_1(self):
        actual = printfrequency([2, 3, 3, 2, 5],5)
        expected = [[2, 2],[3,  2],[5,1]]
        self.assertEqual(actual, expected)

    def test_printfrequency_2(self):
        actual = printfrequency([1, 2, 5, 1, 1, 2, 3, 2],8)
        expected = [[1, 3],[2 ,3],[3,  1],[5, 1]]
        self.assertEqual(actual, expected)

    def test_printfrequency_3(self):
        actual = printfrequency([1, 2, 2],3)
        expected = [[1, 1],[2, 2]]
        self.assertEqual(actual, expected)

    def test_printfrequency_4(self):
        actual = printfrequency([4, 4, 4, 4],4)
        expected = [[4, 4]]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
