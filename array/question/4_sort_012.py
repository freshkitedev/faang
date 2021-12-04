
def sort(array): 
    #Write your code here
    return None

#ok for all test cases required  
import unittest
class Test(unittest.TestCase):

    def test_sort1(self):
        arr = [1,2,0,1,2,1,0]
        sort(arr)
        expected = [0,0,1,1,1,2,2]
        self.assertEqual(arr, expected)

    def test_sort2(self):
        arr = [1,0,2,1,2,0,1,2,1,0]
        actual = sort(arr)
        expected = [0,0,0,1,1,1,1,2,2,2]
        self.assertEqual(arr, expected)

    def test_sort3(self):
        arr = [1,0,2]
        actual = sort(arr)
        expected = [0,1,2]
        self.assertEqual(arr, expected)

    def test_sort4(self):
        arr = [1]
        actual = sort(arr)
        expected = [1]
        self.assertEqual(arr, expected)
    
    def test_sort5(self):
        arr = [2,0]
        actual = sort(arr)
        expected = [0,2]
        self.assertEqual(arr, expected)
unittest.main(verbosity=2)     
