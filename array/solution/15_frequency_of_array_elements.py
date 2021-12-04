# Function to find counts of all elements present in arr[0..n-1]. The array  elements must be range from 1 to n
def printfrequency(arr, n): 
    ret = []
    # Subtract 1 from every element so that the elements become in range from 0 to n-1 
    for j in range(n): 
        arr[j] = arr[j] - 1
   # Use every element arr[i] as index and add 'n' to element present at arr[i]%n to keep track of count of occurrences of arr[i] 
    for i in range(n): 
        arr[arr[i] % n] = arr[arr[i] % n] + n 
    # To print counts, simply print the number of times n was added at index corresponding to every element 
    for i in range(n): 
        if (arr[i] // n) :
            ret.append([i+1, arr[i]//n])
    return ret

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
