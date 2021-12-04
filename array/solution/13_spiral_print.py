# You are given a matrix of m x n elements (m rows, n columns), Print all elements of the matrix in spiral order in O(m*n) Time Complexity and O(1) Space Complexity 
# Asked in : Microsoft, OLA,PayTm, Oracle
def spiralPrint(r, c, matrix) : 
    k = 0; n = 0
    m = c - 1
    p = r - 1 
    ret = [0] * r*c
    t = 0
  # checking k or l lies outside the matrix
    while (k < m and n < p) : 
        # Print First Row
        i = k
        for j in range(k, m) : 
            print(matrix[i][j], end=' ') 
            ret[t] = matrix[i][j]; t += 1
              
        j = m
        # Print Last Column
        for i in range(n, p) : 
            print(matrix[i][j], end=' ')
            ret[t] = matrix[i][j]; t += 1
              
        i = p            
        # Print last row
        for j in range(m, k, -1):
            print(matrix[i][j], end=' ') 
            ret[t] = matrix[i][j]; t += 1
              
        j = k
         # Print the first column 
        for i in range(p, n, -1) : 
            print(matrix[i][j], end=' ') 
            ret[t] = matrix[i][j]; t += 1
              
        k += 1; m -= 1; p -= 1; n += 1

    while (t < r*c):
        print(matrix[n][k], end =' ')
        ret[t] = matrix[n][k]; t += 1
        if (n == p):
            k += 1
        else:
            n += 1

    return ret

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

