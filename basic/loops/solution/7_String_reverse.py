# Write a program to reverse a string.

def reverse_string(n):
    
    s = 0
    e = len(n) - 1
    list_1 = list(n.strip(" "))
    while (s < e):
        
        temp = list_1[s]
        list_1[s] = list_1[e]
        list_1[e] = temp       

        s += 1
        e -= 1  
           
    return (''.join(list_1))
    
    # str = ''
    
    # for i in n:
    #     str = i + str
    # return str


import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual =  reverse_string("santhosh")
        expected = "hsohtnas"
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual =  reverse_string("bala")
        expected = "alab"
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual =  reverse_string("deepika")
        expected = "akipeed"
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = reverse_string("malayalam")
        expected = "malayalam"
        self.assertEqual(actual, expected)
    def test_two_num_sum5(self):
        actual = reverse_string("123")
        expected = "321"
        self.assertEqual(actual, expected)     
    def test_two_num_sum6(self):
        actual = reverse_string("san432e")
        expected = "e234nas"
        self.assertEqual(actual, expected)      
unittest.main(verbosity=2)