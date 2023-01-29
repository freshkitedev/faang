# complete below function to return the sorted array - Bubble sort


def bubble_sort(arr):
    l = len(arr)
    count = 0
   
    for i in range(1 , l):
        for j in range(0, l - i):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Inner loop count:", count)
    return arr

def bubble_sort_efficient(arr):
    l = len(arr)
    count = 0
   
    for i in range(1 , l):
        flag = 0
        for j in range(0, l - i):
            count += 1
            if arr[j] > arr[j + 1]:
                flag = 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag == 0:
            print("Inner loop count:", count)
            return arr

    print("Inner loop count:", count)
    return arr


import unittest

class Test(unittest.TestCase):
    def test_search1(self):
        actual = bubble_sort([3,42,34,5,2])
        expected = [2,3,5,34,42]
        self.assertEqual(actual, expected)
    def test_search2(self):
        actual = bubble_sort([34,9,3,4,-1,-34])
        expected = [-34,-1,3,4,9,34]
        self.assertEqual(actual, expected)
    def test_search3(self):
        actual = bubble_sort([34,9,3,4,-1,-34])
        expected = [-34,-1,3,4,9,34]
        self.assertEqual(actual, expected)
    def test_search3(self):
        actual = bubble_sort([1,2,3,4,5])
        expected = [1,2,3,4,5]
        self.assertEqual(actual, expected)
    def test_search4(self):
        actual = bubble_sort([])
        expected = []
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)