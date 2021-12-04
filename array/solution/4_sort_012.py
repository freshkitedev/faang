
def sort(array): 
    #Write your code here
    zero = 0
    one = 0
    two = 0
    end = len(array)
    for i in range(0, end):
        if (array[i] == 0):
            zero += 1
        if (array[i] == 1):
            one += 1
        if (array[i] == 2):
            two += 1
    
    for i in range(0, end):
        if (zero):
            array[i] = 0
            zero -= 1
        elif (one):
            array[i] = 1
            one -= 1
        else:
            array[i] = 2
            two -= 1
    return None

def swap(array, i1, i2):
    t = array[i1]
    array[i1] = array[i2]
    array[i2] = t
    return None

def sort2(array): 
    #Write your code here
    start = 0
    mid = 0
    end = len(array) - 1

    while (mid <= end):
        if (array[mid] == 2):
            swap(array, mid, end)
            end -= 1
            mid += 1
        elif (array[mid] == 0):
            swap(array, mid, start)
            mid += 1
            start += 1
        else:
            mid += 1

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
