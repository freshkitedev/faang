# complete below function to return the index
# of number n in sorted arr - Binary search - O(logn)

def search(arr, n):
    s = 0
    e = len(arr) - 1
    

    while s <= e:
        m = (s + e) // 2    
        if (arr[m] == n):
            return m
        elif (arr[m] < n):
            s = m + 1
        else:
            e = m - 1
    return -1

def rsearch(arr, s, e, n):
    m = (s+e) // 2

    if (s > e or e == 0 ):
        return -1
    if (arr[m] == n):
        return m
    
    if arr[m] < n:
        return rsearch(arr, m + 1, e, n)
    else:
        return rsearch(arr, s, m - 1, n)


import unittest

class Test(unittest.TestCase):
    def test_search1(self):
        actual = search([3, 5, 7, 42, 54, 75], 54)
        expected = 4
        self.assertEqual(actual, expected)
    def test_search2(self):
        actual = search([3, 5, 7, 42, 54, 75], 5)
        expected = 1
        self.assertEqual(actual, expected)
    def test_search3(self):
        actual = search([3, 5, 7, 42, 54, 75], 75)
        expected = 5
        self.assertEqual(actual, expected)
    def test_search4(self):
        actual = search([3, 5, 7, 42, 54, 75], 3)
        expected = 0
        self.assertEqual(actual, expected)
    def test_search5(self):
        actual = search([3,4, 54], 6)
        expected = -1
        self.assertEqual(actual, expected)
    def test_search6(self):
        actual = search([], 6)
        expected = -1
        self.assertEqual(actual, expected)
    def test_search7(self):
        actual = rsearch([3, 5, 7, 42, 54, 75],0, 5, 54)
        expected = 4
        self.assertEqual(actual, expected)
    def test_search8(self):
        actual = rsearch([3, 5, 7, 42, 54, 75],0,5, 5)
        expected = 1
        self.assertEqual(actual, expected)
    def test_search9(self):
        actual = rsearch([3, 5, 7, 42, 54, 75],0,5, 75)
        expected = 5
        self.assertEqual(actual, expected)
    def test_search10(self):
        actual = rsearch([3, 5, 7, 42, 54, 75],0,5, 3)
        expected = 0
        self.assertEqual(actual, expected)
    def test_search11(self):
        actual = rsearch([3,4, 54],0,2, 6)
        expected = -1
        self.assertEqual(actual, expected)
    def test_search12(self):
        actual = rsearch([],0,0, 6)
        expected = -1
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)