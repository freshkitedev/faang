# Write an algorithm to find out next greater number to given number with the same set of digits 
# Asked in : Morgan Stanley, Makemytrip, Amazon

def swap(arr, i1, i2):
    t = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = t

def sortarr_index(arr, index):
    tmp = arr[index:]
    tmp.sort()
    arr[index:] = tmp

def next_max_num(val):
    num = list(map (int , str(val)))
    n = len(num)
    for i in range(n-1, 0, -1):
        if (num[i-1] < num[i]):
            break

    mindex = i
    for j in range(i+1, n):
        if (num[j] < num[mindex] and num[i-1] < num[j]):
            mindex = j
            
    swap(num, i-1, mindex)
    sortarr_index(num, i)
    res = map(str, num)
    return int("".join(res))

import unittest
class Test(unittest.TestCase):
  
    def test_next_big_num(self):
        actual = next_max_num(15843)
        expected = 18345
        self.assertEqual(actual, expected)

    def test_next_big_num1(self):
        actual = next_max_num(13)
        expected = 31
        self.assertEqual(actual, expected)
    
    def test_next_big_num2(self):
        actual = next_max_num(13843)
        expected = 14338
        self.assertEqual(actual, expected)

    def test_next_big_num3(self):
        actual = next_max_num(12345)
        expected = 12354
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)