#Write a program to print fibonacci series.
def fibonacci(n):
    a=0
    b=1
    c = 0
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        print(a)
        print(b)
        while(c < n):
            c=a+b
            a=b
            b=c
            print(c)
       


fib = fibonacci(5)


# import unittest   
       
# class Test(unittest.TestCase):
#     def test_two_num_sum1(self):
#         actual = fibonacci(10)
#         expected = 011258
#         self.assertEqual(actual, expected)
#     def test_two_num_sum2(self):
#         actual = fibonacci(5)
#         expected = 01123
#         self.assertEqual(actual, expected)
#     def test_two_num_sum3(self):
#         actual = fibonacci(4)
#         expected = 01123
#         self.assertEqual(actual, expected)
#     def test_two_num_sum4(self):
#         actual = fibonacci(n)
#         expected = 
#         self.assertEqual(actual, expected)
# unittest.main(verbosity=2)