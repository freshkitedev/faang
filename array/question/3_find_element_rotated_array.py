# We rotate an ascending order sorted array at some point unknown to user. 
# So for instance, 3 4 5 6 7 might become 5 6 7 3 4. Modify binary search 
# algorithm to find an element in the rotated array in O(log n) time and O(1) Space complexity

def findNumber(array, start, end, value): 
    #Write your code here

#ok for all test cases required  
import unittest
class Test(unittest.TestCase):

    def test_findNumber1(self):
        actual = findNumber([3, 4, 5, 6, 7, 8, 9, 10, 1, 2],0,9,1)
        expected = 8
        self.assertEqual(actual, expected)

    def test_findNumber2(self):
        actual = findNumber([5, 6, 7, 8, 9, 10, 1, 2, 3],0,8,3)
        expected = 8
        self.assertEqual(actual, expected)

    def test_findNumber3(self):
        actual = findNumber([5, 6, 7, 8, 9, 10, 1, 2, 3],0,8,28)
        expected = -1
        self.assertEqual(actual, expected)
    
    def test_findNumber4(self):
        actual = findNumber([30, 40, 50, 10, 20],0,4,10)
        expected = 3
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)     
