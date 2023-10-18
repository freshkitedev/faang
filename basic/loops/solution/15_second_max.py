# Write Program to find second maximum number in list
def second_max_num_in_list(arr):
    l = len(arr)

    if(l <= 1):
        return -1
    max = arr[0]
    secondmax = 0

    for i in range(1,l):
      if(max < arr[i]):
         secondmax = max 
         max = arr[i]
      if(secondmax < arr[i] and max > arr[i]):
         secondmax = arr[i]   
    return secondmax




import unittest

class Test(unittest.TestCase):
    def test_search1(self):
        actual = second_max_num_in_list([3,42,34,5,2])
        expected = 34
        self.assertEqual(actual, expected)
    def test_search2(self):
        actual = second_max_num_in_list([34,9,3,4,-1,-34])
        expected = 9
        self.assertEqual(actual, expected)
    def test_search3(self):
        actual = second_max_num_in_list([34,9,3,4,-1,-34,98])
        expected = 34
        self.assertEqual(actual, expected)
    def test_search4(self):
        actual = second_max_num_in_list([1])
        expected = -1
        self.assertEqual(actual, expected)
    def test_search5(self):
        actual = second_max_num_in_list([-2,-1,0])
        expected = -1
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)