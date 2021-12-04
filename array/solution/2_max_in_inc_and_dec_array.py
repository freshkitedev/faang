# One array of integers is given as an input ,which is initially increasing and 
# then decreasing or it can be only increasing or decreasing , you need to find 
# the maximum value in the array in O(Log n) Time complexity and O(1) Space Complexity 
# Asked in :Amazon Uber Microsoft

def findMaxValue(array, start, end): 
    #Practise yourself : write your code here 
    if (start == end):
        return array[start]
    if (start+1 == end):
        if (array[start] > array[end]):
            return array[start]
        else:
            return array[end]
      
    
    while (start < end):
        mid = start + (end - start) // 2
        if (array[mid] > array[mid-1] and 
            array[mid] > array[mid+1]):
            return array[mid]
        if (array[mid] > array[mid-1] and 
            array[mid] < array[mid+1]):
            # increasing order
            start = mid+1
        if (array[mid] < array[mid-1] and 
            array[mid] > array[mid+1]):
            # decreasing order
            end = mid-1
        
    return array[start]

def findMaxValue2(array, start, end): 
    #Practise yourself : write your code here 
    if (start == end):
        return array[start]
    if (start+1 == end):
        if (array[start] > array[end]):
            return array[start]
        else:
            return array[end]
 
    mid = start + (end - start) // 2
    if (array[mid] > array[mid-1] and 
        array[mid] > array[mid+1]):
        return array[mid]
    if (array[mid] > array[mid-1] and 
        array[mid] < array[mid+1]):
        # increasing order
        return findMaxValue(array, mid+1, end)
    else:
        # decreasing order
        return findMaxValue(array, start, mid-1)

import unittest
class Test(unittest.TestCase):
    def test_findMax1(self):
        array = [43,81,90,54,43,32,21]
        n = len(array)
        actual = findMaxValue(array, 0, n-1)
        expected = 91
        self.assertEqual(actual, expected)
    def test_findMax2(self):
        array = [3,4,6,12,34,56,78]
        n = len(array)
        actual = findMaxValue(array, 0, n-1)
        expected = 78
        self.assertEqual(actual, expected)
    def test_findMax3(self):
        array = [89,78,65,54,43]
        n = len(array)
        actual = findMaxValue(array, 0, n-1)
        expected = 89
        self.assertEqual(actual, expected)
    def test_findMax4(self):
        array = [8]
        n = len(array)
        actual = findMaxValue(array, 0, n-1)
        expected = 8
        self.assertEqual(actual, expected)
    def test_findMax5(self):
        array = [8,12]
        n = len(array)
        actual = findMaxValue(array, 0, n-1)
        expected = 12
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
