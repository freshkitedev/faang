# Given an array nums, write a function to move all 0's to the end 
# of it while maintaining the relative order of the non-zero elements 
# in O(n) Time complexity and O(1) Space complexity with single 
# traversal allowed

import unittest

def swap(arr, i1, i2):
    t = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = t

def MoveZeroToEnd1(array, n): 
    print("Single loop")
    i1 = 0
    i2 = 0
    while (i2 < n):
        if (array[i2] != 0):
            if (i1 != i2):
                swap(array, i1, i2)
            i2 += 1
            i1 += 1
        else:
            i2 += 1
 
    return array

def MoveZeroToEnd(array, n): 
    print("Two loops")
    i1 = 0
    i2 = 0
    while (i2 < n):
        if (array[i2] != 0):
            array[i1] = array[i2]
            i2 += 1
            i1 += 1
        else:
            i2 += 1
    while (i1 < n):
        array[i1] = 0
        i1 += 1
        
    return array

 #ok for all test cases required 
class Test(unittest.TestCase):
  
    def test_MoveZeroToEnd1(self):
        actual = MoveZeroToEnd([1,3,0,0,4,0,9],7)
        expected = [1,3,4,9,0,0,0]
        self.assertEqual(actual, expected)

    def test_MoveZeroToEnd2(self):
        actual = MoveZeroToEnd([0,1,0,3,12],5)
        expected = [1,3,12,0,0]
        self.assertEqual(actual, expected)

    def test_MoveZeroToEnd3(self):
        actual = MoveZeroToEnd([0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9],13)
        expected = [1,9,8,4,2,7,6,9,0,0,0,0,0]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)