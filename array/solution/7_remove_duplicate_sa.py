# Given a sorted array, remove the duplicates in place such that each element appear 
# only once and return the new length. 
#  Time complexity O(n) and Space complexity O(1)

def removeDuplicates(array, n): 
    #Write Your Code Here
    if (n == 0 or n == 1):
        return n
    
    copy_index = 0

    for i in range(0, n-1):
        if (array[i] != array[i+1]):
            array[copy_index] = array[i]
            copy_index += 1
    array[copy_index] = array[n-1]
    copy_index += 1

    return copy_index

import unittest
#ok for all test cases required 
class Test(unittest.TestCase):

    def test_removeDuplicates1(self):
        actual = removeDuplicates([1,1,2],3)
        expected = 2
        self.assertEqual(actual, expected) 

    def test_removeDuplicates2(self):
        actual = removeDuplicates([2, 2, 2, 2, 2],5)
        expected = 1
        self.assertEqual(actual, expected) 

    def test_removeDuplicates3(self):
        actual = removeDuplicates([1, 2, 2, 3, 4, 4, 4, 5, 5],9)
        expected = 5
        self.assertEqual(actual, expected) 

    def test_removeDuplicates4(self):
        actual = removeDuplicates([1,2,3,4,5],5)
        expected = 5
        self.assertEqual(actual, expected) 

unittest.main(verbosity=2)