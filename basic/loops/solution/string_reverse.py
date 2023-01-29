# Write a program to reverse a string.

def reverse (string):
   
    reverse_Str = "" 
    count = len(string)
    while count > 0:   
        reverse_Str = reverse_Str + string[ count - 1 ]
        count = count - 1 
    return reverse_Str  




import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = reverse("hee")
        expected = "eeh"
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual =  reverse("keep")
        expected = "peek"
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = reverse("ok")
        expected = "ko"
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = reverse("key")
        expected = "yek" 
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
