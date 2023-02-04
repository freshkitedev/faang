#Write a Python program to check if a given string is a palindrome
# if string is palindrome means return true or return false

def string_palindrome(n):
    
    s = 0
    e = len(n) - 1
    while (s < e):
     
        if (n[s] == n[e] ):
            s += 1
            e -= 1

        else :
            return False 

    return True    
      





    
   



import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual =  string_palindrome("989")
        expected = True
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual =  string_palindrome("stephan rensog KAVI SANTHOSH muthupandi gautham moni deepi")
        expected = False
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual =  string_palindrome("s")
        expected = True
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = string_palindrome("malayalam")
        expected = True
        self.assertEqual(actual, expected)
    def test_two_num_sum5(self):
        actual = string_palindrome("sts089767564134578098765")
        expected = False
        self.assertEqual(actual, expected)     
    def test_two_num_sum6(self):
        actual = string_palindrome("Z1a1Z")
        expected = True
        self.assertEqual(actual, expected)      
unittest.main(verbosity=2)