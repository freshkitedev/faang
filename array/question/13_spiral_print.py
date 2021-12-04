# You are given a matrix of m x n elements (m rows, n columns), Print all elements of the matrix in spiral order in O(m*n) Time Complexity and O(1) Space Complexity 
# Asked in : Microsoft, OLA,PayTm, Oracle
def spiralPrint(r, c, matrix) : 
    #code here

import unittest

class Test(unittest.TestCase):
    def test_printfrequency_1(self):
        actual = spiralPrint(3,3,[[1,2,3],[4,5,6],[7,8,9]])
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(actual, expected)
    
    def test_printfrequency_4(self):
        actual = spiralPrint(3,2,[[1,2],[4,5],[7,8]])
        expected = [1, 2, 5, 8, 7, 4]
        self.assertEqual(actual, expected)
    
    def test_printfrequency_5(self):
        actual = spiralPrint(4,3,[[1,2,3],[4,5,6],[7,8,9],[11,10,12]])
        expected = [1,2,3,6,9,12,10,11,7,4,5,8]
        self.assertEqual(actual, expected)

    def test_printfrequency_2(self):
        actual = spiralPrint(3,4,[[1,2,3,4],[5,6,7,8],[9,10,11,12]])
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(actual, expected)

    def test_printfrequency_3(self):
        actual = spiralPrint(5,5,[[1, 2, 3, 4, 5],[16, 17, 18, 19, 6],[15, 24, 25, 20, 7],[14, 23, 22, 21, 8],[13, 12, 11, 10, 9]])
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)

